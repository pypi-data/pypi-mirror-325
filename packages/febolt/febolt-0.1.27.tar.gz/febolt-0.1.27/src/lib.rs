// src/lib.rs
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::PyDict;
use numpy::{PyArray1, PyArray2, IntoPyArray};
use ndarray::{
    s, Array, Array1, Array2, ArrayView1, ArrayView2, Axis,
};
use std::collections::HashMap;
use std::f32::consts::{PI, SQRT_2};
use ndarray_linalg::{Inverse, Solve};
use blas::sger;

// -----------------------------------------------------------------------------
// Custom error function approximation for f32
// -----------------------------------------------------------------------------
fn erf(x: f32) -> f32 {
    let a1: f32 = 0.254829592;
    let a2: f32 = -0.284496736;
    let a3: f32 = 1.421413741;
    let a4: f32 = -1.453152027;
    let a5: f32 = 1.061405429;
    let p: f32 = 0.3275911;

    let sign = if x < 0.0 { -1.0 } else { 1.0 };
    let x = x.abs();

    let t = 1.0 / (1.0 + p * x);
    let y = 1.0
        - ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t * (-x * x).exp();
    sign * y
}

// -----------------------------------------------------------------------------
// Simple normal pdf and cdf functions for f32 (using erf)
// -----------------------------------------------------------------------------
#[inline]
fn norm_pdf(z: f32) -> f32 {
    (-0.5 * z * z).exp() / (2.0 * PI).sqrt()
}

#[inline]
fn norm_cdf(z: f32) -> f32 {
    0.5 * (1.0 + erf(z / SQRT_2))
}

// -----------------------------------------------------------------------------
// Probit model implementation using f32
// -----------------------------------------------------------------------------
struct Probit<'a> {
    endog: ArrayView1<'a, f32>,
    exog: ArrayView2<'a, f32>,
}

impl<'a> Probit<'a> {
    fn new(endog: ArrayView1<'a, f32>, exog: ArrayView2<'a, f32>) -> Self {
        Probit { endog, exog }
    }

    #[inline]
    fn cdf(&self, x: f32) -> f32 {
        // clamp to avoid ln(0) in loglike
        let c = 0.5 * (1.0 + erf(x / SQRT_2));
        c.max(1e-15_f32).min(1.0 - 1e-15_f32)
    }

    #[inline]
    fn pdf(&self, x: f32) -> f32 {
        (-0.5 * x * x).exp() / (2.0 * PI).sqrt()
    }

    /// xbeta = X * params
    fn xbeta(&self, params: &ArrayView1<f32>, out: &mut Array1<f32>) {
        *out = self.exog.dot(params);
    }

    /// log-likelihood = sum( ln( Φ(q_i * xbeta_i) ) ), with q_i = 2*y_i - 1
    fn loglike(&self, xbeta: &ArrayView1<f32>) -> f32 {
        let q = self.endog.mapv(|y| 2.0 * y - 1.0);
        q.iter()
            .zip(xbeta.iter())
            .map(|(&qi, &xb)| {
                let val = self.cdf(qi * xb);
                val.ln()
            })
            .sum()
    }

    /// ------------------------------------
    /// Vectorized Score (gradient)
    /// ------------------------------------
    ///
    /// The gradient w.r.t. params is:  X^T * [q_i * pdf(q_i * xbeta_i) / cdf(q_i * xbeta_i)]
    /// factor_i = q_i * (pdf(z_i) / cdf(z_i)), where z_i = q_i * xbeta_i
    fn score(&self, xbeta: &ArrayView1<f32>, grad_out: &mut Array1<f32>) {
        let n = self.exog.nrows();
        let k = self.exog.ncols();
        grad_out.fill(0.0);

        // 1) Compute z_i = q_i * xbeta_i
        let q = self.endog.mapv(|y| 2.0 * y - 1.0);
        let z = &q * xbeta;

        // 2) ratio_i = pdf(z_i)/cdf(z_i)
        let ratio = z.mapv(|zi| {
            let pdf_val = self.pdf(zi);
            let cdf_val = self.cdf(zi);
            pdf_val / cdf_val
        });
        let factor = q * ratio; // elementwise

        // 3) grad = X^T * factor
        // factor is shape (n)
        for j in 0..k {
            let col_j = self.exog.column(j);
            let mut sum_j = 0.0;
            for i in 0..n {
                sum_j += col_j[i] * factor[i];
            }
            grad_out[j] = sum_j;
        }
    }

    /// ------------------------------------
    /// Vectorized Hessian
    /// ------------------------------------
    ///
    /// Hess = - X^T diag(w_i) X,  where
    ///   w_i = ratio_i^2 + ratio_i * z_i,  with ratio_i = pdf(z_i)/cdf(z_i), z_i = q_i * xbeta_i
    fn hessian(&self, xbeta: &ArrayView1<f32>, hess_out: &mut Array2<f32>) {
        let n = self.exog.nrows();
        let k = self.exog.ncols();

        let q = self.endog.mapv(|y| 2.0 * y - 1.0);
        let z = &q * xbeta;
        let ratio = z.mapv(|zi| {
            let pdf_val = self.pdf(zi);
            let cdf_val = self.cdf(zi);
            pdf_val / cdf_val
        });
        let weights = ratio
            .iter()
            .zip(z.iter())
            .map(|(&r, &zi)| r * r + r * zi)
            .collect::<Array1<f32>>();

        hess_out.fill(0.0);
        let mut Xw = self.exog.to_owned(); // copy
        for j in 0..k {
            let mut col_j = Xw.column_mut(j);
            for i in 0..n {
                col_j[i] *= weights[i].sqrt();
            }
        }
        let tmp = Xw.t().dot(&Xw);
        *hess_out = tmp.mapv(|val| -val);
    }

    /// Naive (full) Newton's method with vectorized gradient & Hessian
    fn fit_naive_newton(&self, max_iter: usize, tol: f32) -> (Array1<f32>, f32, bool, usize) {
        let k = self.exog.ncols();
        let mut params = Array1::zeros(k);
        let mut xbeta = Array1::zeros(self.exog.nrows());
        let mut grad = Array1::zeros(k);
        let mut hess = Array2::zeros((k, k));

        self.xbeta(&params.view(), &mut xbeta);
        let mut ll_old = self.loglike(&xbeta.view());
        let mut converged = false;
        let mut iter_used = 0;

        for iter in 0..max_iter {
            iter_used = iter;
            // 1) gradient, 2) Hessian
            self.score(&xbeta.view(), &mut grad);
            self.hessian(&xbeta.view(), &mut hess);

            // Solve Hess * step = grad
            let step = match hess.solve(&grad) {
                Ok(s) => s,
                Err(_) => {
                    eprintln!("Hessian singular at iteration {}", iter);
                    break;
                }
            };

            // params <- params - step
            for j in 0..k {
                params[j] -= step[j];
            }

            // new loglike
            self.xbeta(&params.view(), &mut xbeta);
            let ll_new = self.loglike(&xbeta.view());
            if (ll_new - ll_old).abs() < tol {
                converged = true;
                ll_old = ll_new;
                break;
            }
            ll_old = ll_new;
        }

        (params, ll_old, converged, iter_used)
    }
}

// -----------------------------------------------------------------------------
// Compute robust covariance (White/Eicker-Huber) or cluster-robust
// -----------------------------------------------------------------------------
fn robust_covariance(
    exog: &ArrayView2<f32>,
    xbeta: &ArrayView1<f32>,
    endog: &ArrayView1<f32>,
    h_inv: &ArrayView2<f32>,
    cluster: Option<ArrayView2<f32>>,
) -> Array2<f32> {
    let nobs = exog.nrows();
    let kvars = exog.ncols();

    if cluster.is_none() {
        // White's robust
        let q = endog.mapv(|y| 2.0 * y - 1.0);
        let z = &q * xbeta;

        let mut M_flat = vec![0.0_f32; kvars * kvars];
        for i in 0..nobs {
            let pdf = norm_pdf(z[i]);
            let cdf = norm_cdf(z[i]).max(1e-15_f32).min(1.0 - 1e-15_f32);
            let factor = q[i] * (pdf / cdf);

            // rank-1 update
            let row_vec = exog.row(i);
            let alpha = factor;
            let incx = 1;
            let incy = 1;
            let lda = kvars as i32;
            unsafe {
                sger(
                    kvars as i32,
                    kvars as i32,
                    alpha,
                    row_vec.as_slice().unwrap(),
                    incx,
                    row_vec.as_slice().unwrap(),
                    incy,
                    &mut M_flat,
                    lda,
                );
            }
        }
        let M = Array2::from_shape_vec((kvars, kvars), M_flat)
            .expect("Bad shape for M")
            .reversed_axes();
        h_inv.dot(&M).dot(h_inv)
    } else {
        // cluster-robust
        let cluster = cluster.unwrap();
        let q = endog.mapv(|y| 2.0 * y - 1.0);
        let z = &q * xbeta;
        let mut M = Array2::<f32>::zeros((kvars, kvars));

        if cluster.ncols() != 1 {
            // multi-column => treat as White
            for i in 0..nobs {
                let pdf = norm_pdf(z[i]);
                let cdf = norm_cdf(z[i]).max(1e-15_f32).min(1.0 - 1e-15_f32);
                let factor = q[i] * (pdf / cdf);
                let row = exog.row(i);
                for j in 0..kvars {
                    let xj = row[j] * factor;
                    for k_ in 0..kvars {
                        M[(j, k_)] += xj * row[k_];
                    }
                }
            }
        } else {
            // single clustering
            let mut cluster_map: HashMap<u32, Array1<f32>> = HashMap::new();
            for i in 0..nobs {
                let cl_val = cluster[[i, 0]];
                let key = cl_val.to_bits();
                let pdf = norm_pdf(z[i]);
                let cdf = norm_cdf(z[i]).max(1e-15_f32).min(1.0 - 1e-15_f32);
                let factor = q[i] * (pdf / cdf);

                let row = exog.row(i);
                let entry = cluster_map.entry(key).or_insert_with(|| Array1::zeros(kvars));
                for (g, &x) in entry.iter_mut().zip(row.iter()) {
                    *g += x * factor;
                }
            }
            // sum outer products
            for score in cluster_map.values() {
                let outer = score.view().insert_axis(Axis(1)).dot(
                    &score.view().insert_axis(Axis(0))
                );
                M += &outer;
            }
        }
        h_inv.dot(&M).dot(h_inv)
    }
}

// -----------------------------------------------------------------------------
// Helper function: run the fitting, compute covariance, etc.
// -----------------------------------------------------------------------------
fn model_fit<'a>(
    exog: &'a Array2<f32>,
    endog: ArrayView1<'a, f32>,
    max_iter: usize,
    tol: f32,
    robust: bool,
    cluster_vars: Option<&PyAny>,
) -> PyResult<(Array1<f32>, f32, bool, usize, Array2<f32>)> {
    let probit = Probit::new(endog, exog.view());
    let (params, llf, converged, iterations) = probit.fit_naive_newton(max_iter, tol);

    // Evaluate Hessian at final
    let mut xbeta = Array1::zeros(exog.nrows());
    probit.xbeta(&params.view(), &mut xbeta);

    let mut hess = Array2::zeros((params.len(), params.len()));
    probit.hessian(&xbeta.view(), &mut hess);

    let mut cov_final = match hess.inv() {
        Ok(inv_hess) => -inv_hess, // Hess is negative => invert => times -1
        Err(_) => {
            eprintln!("Hessian is singular => using identity for covariance");
            -Array2::<f32>::eye(exog.ncols())
        }
    };

    // robust cov?
    if robust {
        let cluster_view = if let Some(obj) = cluster_vars {
            let arr_2d = obj.downcast::<PyArray2<f32>>()?;
            let view = unsafe { arr_2d.as_array() };
            if view.nrows() != exog.nrows() {
                return Err(PyErr::new::<pyo3::exceptions::PyValueError, _>(
                    format!("Cluster vars has {} rows, expected {}", view.nrows(), exog.nrows()),
                ));
            }
            Some(view)
        } else {
            None
        };
        let h_inv = cov_final.mapv(|x| -x); // multiply by -1 again => H_inv
        cov_final = robust_covariance(&exog.view(), &xbeta.view(), &probit.endog, &h_inv.view(), cluster_view);
    }

    Ok((params, llf, converged, iterations, cov_final))
}

// -----------------------------------------------------------------------------
// PyO3 classes
// -----------------------------------------------------------------------------
#[pyclass]
#[derive(Clone)]
struct RustProbitModel {
    exog_: Py<PyArray2<f32>>,
    endog_: Py<PyArray1<f32>>,
    exog_names_: Vec<String>,
}

#[pymethods]
impl RustProbitModel {
    #[getter]
    fn exog(&self) -> Py<PyArray2<f32>> {
        self.exog_.clone()
    }
    #[getter]
    fn endog(&self) -> Py<PyArray1<f32>> {
        self.endog_.clone()
    }
    #[getter]
    fn exog_names(&self) -> Vec<String> {
        self.exog_names_.clone()
    }
}

#[pyclass]
struct RustProbitResults {
    params_: Py<PyArray1<f32>>,
    cov_: Py<PyArray2<f32>>,
    model_: RustProbitModel,
    loglike_: f32,
    iterations_: usize,
    converged_: bool,
}

#[pymethods]
impl RustProbitResults {
    #[getter]
    fn params(&self) -> Py<PyArray1<f32>> {
        self.params_.clone()
    }
    #[getter]
    fn cov_params(&self) -> Py<PyArray2<f32>> {
        self.cov_.clone()
    }
    #[getter]
    fn model(&self) -> RustProbitModel {
        self.model_.clone()
    }
    #[getter]
    fn loglike(&self) -> f32 {
        self.loglike_
    }
    #[getter]
    fn iterations(&self) -> usize {
        self.iterations_
    }
    #[getter]
    fn converged(&self) -> bool {
        self.converged_
    }
}

// -----------------------------------------------------------------------------
// fit_probit: Python-facing entry point
// -----------------------------------------------------------------------------
#[pyfunction]
#[allow(clippy::too_many_arguments)]
fn fit_probit(
    py: Python<'_>,
    endog_py: &PyAny,
    exog_py: &PyAny,
    max_iter: Option<usize>,
    tol: Option<f32>,
    robust: Option<bool>,
    cluster_vars: Option<&PyAny>,
    intercept: Option<bool>,
) -> PyResult<RustProbitResults> {
    // Convert endog to float32 if needed, flatten if shape is (N,1)
    let endog_py = {
        let dtype = endog_py.getattr("dtype")?.str()?.to_str()?;
        if dtype.contains("float64") {
            endog_py.call_method1("astype", ("float32",))?
        } else {
            endog_py.into()
        }
    };
    let endog_py = {
        let shape: Vec<usize> = endog_py.getattr("shape")?.extract()?;
        if shape.len() == 2 && shape[1] == 1 {
            endog_py.call_method0("flatten")?
        } else {
            endog_py.into()
        }
    };

    // Convert exog to float32
    let exog_py = {
        let dtype = exog_py.getattr("dtype")?.str()?.to_str()?;
        if dtype.contains("float64") {
            exog_py.call_method1("astype", ("float32",))?
        } else {
            exog_py.into()
        }
    };

    let exog_py_array = exog_py.downcast::<PyArray2<f32>>()?;
    let endog_py_array = if let Ok(arr) = endog_py.downcast::<PyArray1<f32>>() {
        arr
    } else {
        let dyn_arr = endog_py.downcast::<numpy::PyArrayDyn<f32>>()?;
        unsafe {
            dyn_arr
                .as_array()
                .into_dimensionality::<ndarray::Ix1>()
                .map_err(|_| {
                    PyErr::new::<pyo3::exceptions::PyValueError, _>(
                        "Could not convert endog to 1D f32 array",
                    )
                })?
                .into_owned()
                .into_pyarray(py)
        }
    };

    let endog_view = unsafe { endog_py_array.as_array() };
    let exog_view = unsafe { exog_py_array.as_array() };

    let intercept = intercept.unwrap_or(true);
    let exog_with_intercept = if intercept {
        let nobs = exog_view.nrows();
        let ones = ndarray::Array2::ones((nobs, 1));
        ndarray::concatenate(Axis(1), &[ones.view(), exog_view]).map_err(|e| {
            PyErr::new::<pyo3::exceptions::PyValueError, _>(format!(
                "Concatenate intercept failed: {}",
                e
            ))
        })?
    } else {
        exog_view.to_owned()
    };

    // exog_names
    let exog_names = if intercept {
        let mut names = vec!["Intercept".to_string()];
        for j in 0..(exog_with_intercept.ncols() - 1) {
            names.push(format!("x{}", j));
        }
        names
    } else {
        (0..exog_with_intercept.ncols())
            .map(|j| format!("x{}", j))
            .collect()
    };

    // Fit model
    let endog_for_fit = endog_view.to_owned();
    let (params, llf, converged, iterations, cov_final) = model_fit(
        &exog_with_intercept,
        endog_for_fit.view(),
        max_iter.unwrap_or(35),
        tol.unwrap_or(1e-6),
        robust.unwrap_or(false),
        cluster_vars,
    )?;

    // Convert to Py objects
    let params_py = PyArray1::from_owned_array(py, params).into();
    let cov_py = PyArray2::from_owned_array(py, cov_final).into();
    let exog_py_owned = PyArray2::from_owned_array(py, exog_with_intercept).into();
    let endog_py_owned = PyArray1::from_owned_array(py, endog_for_fit).into();

    Ok(RustProbitResults {
        params_: params_py,
        cov_: cov_py,
        model_: RustProbitModel {
            exog_: exog_py_owned,
            endog_: endog_py_owned,
            exog_names_: exog_names,
        },
        loglike_: llf,
        iterations_: iterations,
        converged_: converged,
    })
}

// -----------------------------------------------------------------------------
// AME (Average Marginal Effects) function using f32
// -----------------------------------------------------------------------------
fn add_significance_stars(p: f32) -> &'static str {
    if p < 0.01 {
        "***"
    } else if p < 0.05 {
        "**"
    } else if p < 0.1 {
        "*"
    } else {
        ""
    }
}

#[pyfunction]
fn ame<'py>(
    py: Python<'py>,
    probit_model: &'py PyAny,
    chunk_size: Option<usize>,
) -> PyResult<&'py PyAny> {
    // 1) Extract final params & covariance
    let params_obj = probit_model.getattr("params")?;
    let beta_view = params_obj.downcast::<PyArray1<f32>>()?;
    let beta = unsafe { beta_view.as_array() }.to_owned();

    let cov_obj = probit_model.getattr("cov_params")?;
    let cov_view = cov_obj.downcast::<PyArray2<f32>>()?;
    let cov_beta = unsafe { cov_view.as_array() }.to_owned();

    // 2) Extract exog names & exog
    let mut exog_names: Vec<String> = probit_model
        .getattr("model")?
        .getattr("exog_names")?
        .extract()?;

    let x_obj = probit_model.getattr("model")?.getattr("exog")?;
    let X = unsafe { x_obj.downcast::<PyArray2<f32>>()?.as_array() };
    let (n, k) = (X.nrows(), X.ncols());
    let chunk = chunk_size.unwrap_or(n);

    // Identify intercept columns
    let mut intercept_indices: Vec<usize> = exog_names
        .iter()
        .enumerate()
        .filter_map(|(i, nm)| {
            let nm_lower = nm.to_lowercase();
            if nm_lower == "const" || nm_lower == "intercept" {
                Some(i)
            } else {
                None
            }
        })
        .collect();
    // if any column is constant, label it intercept
    for j in 0..k {
        let col = X.column(j);
        let first_val = col[0];
        let all_same = col.iter().all(|&v| (v - first_val).abs() < 1e-12);
        if all_same && !intercept_indices.contains(&j) {
            intercept_indices.push(j);
            exog_names[j] = "Intercept".to_string();
        }
    }

    // Identify discrete columns (0/1) except intercept
    let is_discrete: Vec<usize> = (0..k)
        .filter(|&j| {
            if intercept_indices.contains(&j) {
                false
            } else {
                X.column(j).iter().all(|&v| v == 0.0 || v == 1.0)
            }
        })
        .collect();

    // We'll accumulate partial sums in a chunked loop
    let mut sum_ame = vec![0.0_f32; k];
    let mut partial_jl_sums = vec![0.0_f32; k * k];

    let mut idx_start = 0;
    while idx_start < n {
        let idx_end = (idx_start + chunk).min(n);
        let x_chunk = X.slice(s![idx_start..idx_end, ..]);
        let n_c = x_chunk.nrows();

        // z_chunk = x_chunk dot beta
        let z_chunk = x_chunk.dot(&beta);
        // phi(z)
        let phi_vals = z_chunk.mapv(norm_pdf);

        // -------------------
        // 1) discrete columns
        // -------------------
        for &j in &is_discrete {
            if intercept_indices.contains(&j) {
                continue;
            }
            let xj_col = x_chunk.column(j);
            let beta_j = beta[j];

            // Delta for going from 0 -> 1
            let delta_j1 = xj_col.mapv(|x| if x == 0.0 { beta_j } else { 0.0 });
            let delta_j0 = xj_col.mapv(|x| if x == 1.0 { -beta_j } else { 0.0 });

            let z_j1 = &z_chunk + &delta_j1;
            let z_j0 = &z_chunk + &delta_j0;

            let cdf_j1 = z_j1.mapv(norm_cdf);
            let cdf_j0 = z_j0.mapv(norm_cdf);

            let cdf_diff_sum = cdf_j1.sum() - cdf_j0.sum();
            sum_ame[j] += cdf_diff_sum;

            let pdf_j1 = z_j1.mapv(norm_pdf);
            let pdf_j0 = z_j0.mapv(norm_pdf);
            let diff_pdf = &pdf_j1 - &pdf_j0;

            // partial derivative wrt beta_l
            // if l==j => pdf_j1.sum()
            // else => diff_pdf dot X[:,l]
            for l in 0..k {
                if l == j {
                    partial_jl_sums[j * k + l] += pdf_j1.sum();
                } else {
                    let col_l = x_chunk.column(l);
                    let dot_val = diff_pdf.dot(&col_l);
                    partial_jl_sums[j * k + l] += dot_val;
                }
            }
        }

        // -------------------
        // 2) continuous columns
        // -------------------
        for j in 0..k {
            if intercept_indices.contains(&j) || is_discrete.contains(&j) {
                continue;
            }
            let beta_j = beta[j];
            // sum of marginal effect = beta_j * sum(phi(z_i))
            let sum_phi = phi_vals.sum();
            sum_ame[j] += beta_j * sum_phi;

            // Now we want partial wrt each beta_l
            // derivative of [beta_j * phi(z_i)] wrt beta_l:
            // = if l==j => sum_phi + ...
            //   plus beta_j * sum_i [phi'(z_i)* x_il]
            // but phi'(z) for normal pdf is -z * phi(z)
            // => pprime[i] = -z_i * phi_vals[i]
            let pprime = (&z_chunk * &phi_vals) * -1.0;

            // We'll build M = x_chunk scaled rowwise by pprime[i]
            let mut M = x_chunk.to_owned();
            for (i, mut row_i) in M.outer_iter_mut().enumerate() {
                let scale = pprime[i];
                row_i.mapv_inplace(|val| val * scale);
            }
            // Now col_sums = sum of each column
            let col_sums = M.sum_axis(Axis(0));

            // partial_jl_sums[j,k] =  (if l==j => + sum_phi) + beta_j * col_sums[l]
            for l in 0..k {
                let mut val = beta_j * col_sums[l];
                if l == j {
                    val += sum_phi;
                }
                partial_jl_sums[j * k + l] += val;
            }
        }

        idx_start = idx_end;
    }

    // Finally, average them
    let ame: Vec<f32> = sum_ame.iter().map(|v| v / n as f32).collect();

    // Construct gradient(AME) matrix
    let mut grad_ame = Array2::zeros((k, k));
    for j in 0..k {
        for l in 0..k {
            grad_ame[(j, l)] = partial_jl_sums[j * k + l] / (n as f32);
        }
    }

    // Cov(AME) = grad_ame * Cov(beta) * grad_ame^T
    let cov_ame = grad_ame.dot(&cov_beta).dot(&grad_ame.t());
    let var_ame: Vec<f32> = cov_ame.diag().iter().map(|&v| v.max(0.0)).collect();
    let se_ame: Vec<f32> = var_ame.iter().map(|v| v.sqrt()).collect();

    // Prepare final table
    let (mut dy_dx, mut se_err, mut z_vals, mut p_vals, mut sig, mut names) =
        (Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new());

    for j in 0..k {
        // skip intercept(s)
        if intercept_indices.contains(&j) {
            continue;
        }
        let val = ame[j];
        let se = se_ame[j];
        let z = if se > 0.0 { val / se } else { f32::NAN };
        let p = 2.0 * (1.0 - norm_cdf(z.abs()));

        dy_dx.push(val);
        se_err.push(se);
        z_vals.push(z);
        p_vals.push(p);
        sig.push(add_significance_stars(p));
        names.push(exog_names[j].clone());
    }

    // Build pandas DataFrame
    let pd = py.import("pandas")?;
    let data = pyo3::types::PyDict::new(py);
    data.set_item("dy/dx", dy_dx)?;
    data.set_item("Std. Err", se_err)?;
    data.set_item("z", z_vals)?;
    data.set_item("Pr(>|z|)", p_vals)?;
    data.set_item("Significance", sig)?;

    let kwargs = pyo3::types::PyDict::new(py);
    kwargs.set_item("data", data)?;
    kwargs.set_item("index", names)?;

    pd.call_method("DataFrame", (), Some(kwargs))
}

// -----------------------------------------------------------------------------
// PyO3 Module Definition
// -----------------------------------------------------------------------------
#[pymodule]
fn febolt(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(fit_probit, m)?)?;
    m.add_function(wrap_pyfunction!(ame, m)?)?;
    Ok(())
}

