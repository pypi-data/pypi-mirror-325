// src/lib.rs
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::PyDict; // imported for later use if needed
use numpy::{PyArray1, PyArray2};
use ndarray::{Array1, Array2, ArrayView1, ArrayView2, Axis, s};
use std::f32::consts::{PI, SQRT_2};
use std::collections::HashMap;
use ndarray_linalg::{Solve, Inverse};
use std::error::Error as StdError;
use std::fmt;

// Import the math traits from argmin-math.
use argmin_math::{
    ArgminSub, ArgminAdd, ArgminMul, ArgminDot, ArgminZeroLike,
    ArgminL1Norm, ArgminL2Norm, ArgminSignum, ArgminMinMax,
};

use argmin::core::{CostFunction, Gradient, Executor, OptimizationResult, Solver};
use argmin::solver::quasinewton::LBFGS;
use argmin::solver::linesearch::MoreThuenteLineSearch;

// ---------------------------
// Some helper math functions
// ---------------------------

#[inline]
fn logistic(x: f32) -> f32 {
    1.0 / (1.0 + (-x).exp())
}

#[inline]
fn norm_pdf(x: f32) -> f32 {
    (-0.5 * x * x).exp() / (2.0 * PI).sqrt()
}

#[inline]
fn norm_cdf(x: f32) -> f32 {
    // using an approximate error function
    let a1 = 0.254829592_f32;
    let a2 = -0.284496736_f32;
    let a3 = 1.421413741_f32;
    let a4 = -1.453152027_f32;
    let a5 = 1.061405429_f32;
    let p  = 0.3275911_f32;
    let sign = if x < 0.0 { -1.0 } else { 1.0 };
    let abs_x = x.abs();
    let t = 1.0/(1.0+p*abs_x);
    let y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t*(-abs_x*abs_x).exp();
    0.5*(1.0+ sign*y)
}

// ---------------------------
// Define our cost functions
// ---------------------------

/// For Logit regression: we assume that y is encoded as ±1.
/// The cost is:
///   J(β) = - Σ log ( σ( yᵢ (xᵢ·β) ) ) + (α/2)||β||² .
struct LogitProblem {
    x: Array2<f32>, // shape (n_samples, n_features)
    y: Array1<f32>, // shape (n_samples,), values: -1.0 or 1.0
    alpha: f32,     // regularization weight
}

impl CostFunction for LogitProblem {
    type Param = Array1<f32>;
    type Output = f32;
    fn cost(&self, param: &Self::Param) -> Result<f32, argmin::core::Error> {
        let z = self.x.dot(param);
        let mut cost = 0.0;
        for (&yi, &zi) in self.y.iter().zip(z.iter()) {
            let arg = yi * zi;
            let sigma = logistic(arg).max(1e-15);
            cost -= sigma.ln();
        }
        cost += 0.5 * self.alpha * param.dot(param);
        Ok(cost)
    }
}

impl Gradient for LogitProblem {
    type Param = Array1<f32>;
    type Gradient = Array1<f32>;
    fn gradient(&self, param: &Self::Param) -> Result<Self::Gradient, argmin::core::Error> {
        let z = self.x.dot(param);
        let n = self.x.nrows();
        let mut grad = Array1::<f32>::zeros(param.len());
        for i in 0..n {
            let yi = self.y[i];
            let zi = z[i];
            let sigma = logistic(yi * zi);
            let factor = -yi * (1.0 - sigma);
            let xi = self.x.row(i);
            grad.scaled_add(factor, &xi);
        }
        grad.scaled_add(self.alpha, param);
        Ok(grad)
    }
}

/// For Probit regression: we assume that y is encoded as ±1.
/// The cost is:
///   J(β) = - Σ log ( Φ( yᵢ (xᵢ·β) ) )
struct ProbitProblem {
    x: Array2<f32>,
    y: Array1<f32>,
}

impl CostFunction for ProbitProblem {
    type Param = Array1<f32>;
    type Output = f32;
    fn cost(&self, param: &Self::Param) -> Result<f32, argmin::core::Error> {
        let z = self.x.dot(param);
        let mut cost = 0.0;
        for (&yi, &zi) in self.y.iter().zip(z.iter()) {
            let arg = yi * zi;
            let phi = norm_cdf(arg).max(1e-15);
            cost -= phi.ln();
        }
        Ok(cost)
    }
}

impl Gradient for ProbitProblem {
    type Param = Array1<f32>;
    type Gradient = Array1<f32>;
    fn gradient(&self, param: &Self::Param) -> Result<Self::Gradient, argmin::core::Error> {
        let z = self.x.dot(param);
        let n = self.x.nrows();
        let mut grad = Array1::<f32>::zeros(param.len());
        for i in 0..n {
            let yi = self.y[i];
            let zi = z[i];
            let arg = yi * zi;
            let phi_val = norm_pdf(arg);
            let cdf_val = norm_cdf(arg).max(1e-15);
            let factor = -yi * (phi_val / cdf_val);
            let xi = self.x.row(i);
            grad.scaled_add(factor, &xi);
        }
        Ok(grad)
    }
}

// ---------------------------
// Hessian computations (analytic)
// ---------------------------
fn hessian_logit(x: &ArrayView2<f32>, param: &ArrayView1<f32>, alpha: f32) -> Array2<f32> {
    let z = x.dot(param);
    let n_features = x.ncols();
    let mut hess = Array2::<f32>::zeros((n_features, n_features));
    for (i, &zi) in z.iter().enumerate() {
        let sigma = logistic(zi);
        let weight = sigma * (1.0 - sigma);
        let xi = x.row(i);
        let outer = xi.to_owned().insert_axis(Axis(1))
                    .dot(&xi.to_owned().insert_axis(Axis(0)));
        hess = hess + weight * outer;
    }
    for i in 0..n_features {
        hess[(i, i)] += alpha;
    }
    hess
}

fn hessian_probit(x: &ArrayView2<f32>, param: &Array1<f32>) -> Array2<f32> {
    let z = x.dot(param);
    let n_features = x.ncols();
    let mut hess = Array2::<f32>::zeros((n_features, n_features));
    for (i, &zi) in z.iter().enumerate() {
        let cdf = norm_cdf(zi).max(1e-15);
        let pdf = norm_pdf(zi);
        let weight = (pdf * pdf) / (cdf * cdf) + (pdf * zi) / cdf;
        let xi = x.row(i);
        let outer = xi.to_owned().insert_axis(Axis(1))
                    .dot(&xi.to_owned().insert_axis(Axis(0)));
        hess = hess - weight * outer;
    }
    hess
}

// ---------------------------
// LBFGS solver helper function
// ---------------------------
fn run_lbfgs<P>(problem: P, init: Array1<f32>, max_iters: u64)
    -> Result<Array1<f32>, Box<dyn StdError>>
where
    P: CostFunction<Param = Array1<f32>, Output = f32> 
      + Gradient<Param = Array1<f32>, Gradient = Array1<f32>>,
{
    let linesearch = MoreThuenteLineSearch::new();
    let solver = LBFGS::new(linesearch, 10);
    // Let the types be inferred.
    let res = Executor::new(problem, solver)
        .configure(|state| state.param(init).max_iters(max_iters))
        .run()?;
    Ok(res.state.best_param.unwrap())
}

// ---------------------------
// PyO3 model/result classes
// ---------------------------
#[pyclass]
#[derive(Clone)]
struct RustLogitModel {
    exog_: Py<PyArray2<f32>>,
    endog_: Py<PyArray1<f32>>,
    exog_names_: Vec<String>,
    model_type_: String, // "logit"
}

#[pymethods]
impl RustLogitModel {
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
    #[getter]
    fn model_type(&self) -> &str {
        &self.model_type_
    }
}

#[pyclass]
struct RustLogitResults {
    params_: Py<PyArray1<f32>>,
    cov_: Py<PyArray2<f32>>,
    model_: RustLogitModel,
    loglike_: f32,
    iterations_: u64,
}

#[pymethods]
impl RustLogitResults {
    #[getter]
    fn params(&self) -> Py<PyArray1<f32>> {
        self.params_.clone()
    }
    #[getter]
    fn cov_params(&self) -> Py<PyArray2<f32>> {
        self.cov_.clone()
    }
    #[getter]
    fn model(&self) -> RustLogitModel {
        self.model_.clone()
    }
    #[getter]
    fn loglike(&self) -> f32 {
        self.loglike_
    }
    #[getter]
    fn iterations(&self) -> u64 {
        self.iterations_
    }
}

#[pyclass]
#[derive(Clone)]
struct RustProbitModel {
    exog_: Py<PyArray2<f32>>,
    endog_: Py<PyArray1<f32>>,
    exog_names_: Vec<String>,
    model_type_: String, // "probit"
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
    #[getter]
    fn model_type(&self) -> &str {
        &self.model_type_
    }
}

#[pyclass]
struct RustProbitResults {
    params_: Py<PyArray1<f32>>,
    cov_: Py<PyArray2<f32>>,
    model_: RustProbitModel,
    loglike_: f32,
    iterations_: u64,
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
    fn iterations(&self) -> u64 {
        self.iterations_
    }
}

// ---------------------------
// PyO3 fit functions
// ---------------------------
#[pyfunction]
#[allow(clippy::too_many_arguments)]
fn fit_logit(
    py: Python,
    endog_py: &PyAny,
    exog_py: &PyAny,
    max_iter: Option<u64>,
    intercept: Option<bool>,
    alpha: Option<f32>,
) -> PyResult<RustLogitResults> {
    let intercept = intercept.unwrap_or(true);
    let alpha = alpha.unwrap_or(0.0);
    let endog_py = endog_py.call_method0("flatten")?;
    let endog_array = endog_py.downcast::<PyArray1<f32>>()?;
    let mut exog_array = exog_py.downcast::<PyArray2<f32>>()?.to_owned_array();

    if intercept {
        let n = exog_array.nrows();
        let ones = Array2::ones((n, 1));
        exog_array = ndarray::concatenate(Axis(1), &[ones.view(), exog_array.view()])
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{}", e)))?;
    }
    // Map original y (assumed coded as 0/1) to -1/1.
    let y_vec: Vec<f32> = unsafe { endog_array.as_array() }
        .iter()
        .map(|&v| if v < 0.5 { -1.0 } else { 1.0 })
        .collect();
    let y = Array1::from(y_vec);
    let n_features = exog_array.ncols();
    let init = Array1::<f32>::zeros(n_features);

    let problem = LogitProblem {
        x: exog_array.clone(),
        y: y.clone(),
        alpha,
    };
    let max_iter = max_iter.unwrap_or(100);
    let opt_param = run_lbfgs(problem, init, max_iter)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("LBFGS error: {}", e)))?;
    let loglike = -LogitProblem { x: exog_array.clone(), y: y.clone(), alpha }
        .cost(&opt_param)
        .unwrap();
    let hess = hessian_logit(&exog_array.view(), &opt_param.view(), alpha);
    let cov = hess.inv().unwrap_or_else(|_| Array2::<f32>::eye(n_features));

    // Prepare column names.
    let mut exog_names = Vec::new();
    if intercept {
        exog_names.push("intercept".to_string());
    }
    for i in 0..(n_features - intercept as usize) {
        exog_names.push(format!("x{}", i));
    }
    // Convert owned arrays into Py objects using from_owned_array(...).to_owned()
    let params_py = PyArray1::from_owned_array(py, opt_param).to_owned();
    let cov_py = PyArray2::from_owned_array(py, cov).to_owned();
    let exog_py_owned = PyArray2::from_owned_array(py, exog_array).to_owned();
    let endog_array_owned = endog_array.to_owned_array();
    let endog_py_owned = PyArray1::from_owned_array(py, endog_array_owned).into();
    Ok(RustLogitResults {
        params_: params_py,
        cov_: cov_py,
        model_: RustLogitModel {
            exog_: exog_py_owned,
            endog_: endog_py_owned,
            exog_names_: exog_names,
            model_type_: "logit".to_string(),
        },
        loglike_: loglike,
        iterations_: max_iter,
    })
}

#[pyfunction]
#[allow(clippy::too_many_arguments)]
fn fit_probit(
    py: Python,
    endog_py: &PyAny,
    exog_py: &PyAny,
    max_iter: Option<u64>,
    intercept: Option<bool>,
) -> PyResult<RustProbitResults> {
    let intercept = intercept.unwrap_or(true);
    let endog_py = endog_py.call_method0("flatten")?;
    let endog_array = endog_py.downcast::<PyArray1<f32>>()?;
    let mut exog_array = exog_py.downcast::<PyArray2<f32>>()?.to_owned_array();

    if intercept {
        let n = exog_array.nrows();
        let ones = Array2::ones((n, 1));
        exog_array = ndarray::concatenate(Axis(1), &[ones.view(), exog_array.view()])
            .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("{}", e)))?;
    }
    let y_vec: Vec<f32> = unsafe { endog_array.as_array() }
        .iter()
        .map(|&v| if v < 0.5 { -1.0 } else { 1.0 })
        .collect();
    let y = Array1::from(y_vec);
    let n_features = exog_array.ncols();
    let init = Array1::<f32>::zeros(n_features);

    let problem = ProbitProblem {
        x: exog_array.clone(),
        y: y.clone(),
    };
    let max_iter = max_iter.unwrap_or(100);
    // Pass a reference to opt_param (which is owned) directly.
    let opt_param = run_lbfgs(problem, init, max_iter)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("LBFGS error: {}", e)))?;
    let loglike = -ProbitProblem { x: exog_array.clone(), y: y.clone() }
        .cost(&opt_param)
        .unwrap();
    let hess = hessian_probit(&exog_array.view(), &opt_param);
    let cov = hess.inv().unwrap_or_else(|_| Array2::<f32>::eye(n_features));

    let mut exog_names = Vec::new();
    if intercept {
        exog_names.push("intercept".to_string());
    }
    for i in 0..(n_features - intercept as usize) {
        exog_names.push(format!("x{}", i));
    }
    let params_py = PyArray1::from_owned_array(py, opt_param).to_owned();
    let cov_py = PyArray2::from_owned_array(py, cov).to_owned();
    let exog_py_owned = PyArray2::from_owned_array(py, exog_array).to_owned();
    let endog_array_owned = endog_array.to_owned_array();
    let endog_py_owned = PyArray1::from_owned_array(py, endog_array_owned).into();
    Ok(RustProbitResults {
        params_: params_py,
        cov_: cov_py,
        model_: RustProbitModel {
            exog_: exog_py_owned,
            endog_: endog_py_owned,
            exog_names_: exog_names,
            model_type_: "probit".to_string(),
        },
        loglike_: loglike,
        iterations_: max_iter,
    })
}
// -----------------------------------------------------------------------------
// Helper functions for the AME function (unchanged)
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

fn as_array2_f32<'py>(obj: &'py PyAny) -> PyResult<ndarray::ArrayView2<'py, f32>> {
    let pyarray = obj.downcast::<PyArray2<f32>>()?;
    unsafe { Ok(pyarray.as_array()) }
}

fn as_array1_f32<'py>(obj: &'py PyAny) -> PyResult<ndarray::ArrayView1<'py, f32>> {
    let pyarray = obj.downcast::<PyArray1<f32>>()?;
    unsafe { Ok(pyarray.as_array()) }
}

// -----------------------------------------------------------------------------
// AME (Average Marginal Effects) function using f32
// -----------------------------------------------------------------------------
#[pyfunction]
fn ame<'py>(
    py: Python<'py>,
    model_result: &'py PyAny,  // Can be a probit or logit results object
    chunk_size: Option<usize>, // Optional chunk size for processing
) -> PyResult<&'py PyAny> {
    // Get beta and covariance parameters from the results object
    let params_obj = model_result.getattr("params")?;
    let beta_view = params_obj.downcast::<PyArray1<f32>>()?;
    let beta = unsafe { beta_view.as_array() }.to_owned();

    let cov_obj = model_result.getattr("cov_params")?;
    let cov_view = cov_obj.downcast::<PyArray2<f32>>()?;
    let cov_beta = unsafe { cov_view.as_array() }.to_owned();

    // Retrieve exogenous variable names and exog matrix from the embedded model.
    let model = model_result.getattr("model")?;
    let mut exog_names: Vec<String> = model.getattr("exog_names")?.extract()?;
    
    let x_obj = model.getattr("exog")?;
    let X = unsafe { x_obj.downcast::<PyArray2<f32>>()?.as_array() };

    // Determine model type (probit or logit) from the model's property.
    let model_type: String = model.getattr("model_type")?.extract()?;
    
    // Define the appropriate pdf and cdf functions.
    let (pdf_fn, cdf_fn): (Box<dyn Fn(f32) -> f32>, Box<dyn Fn(f32) -> f32>) = 
        if model_type.to_lowercase() == "logit" {
            (Box::new(|z: f32| {
                let ex = (-z).exp();
                ex / ((1.0 + ex) * (1.0 + ex))
            }),
             Box::new(|z: f32| {
                let c = 1.0 / (1.0 + (-z).exp());
                c.max(1e-15_f32).min(1.0 - 1e-15_f32)
             }))
        } else {
            (Box::new(|z: f32| norm_pdf(z)),
             Box::new(|z: f32| norm_cdf(z)))
        };

    let (n, k) = (X.nrows(), X.ncols());
    let chunk = chunk_size.unwrap_or(n);

    let mut intercept_indices: Vec<usize> = exog_names
        .iter()
        .enumerate()
        .filter_map(|(i, nm)| {
            let ln = nm.to_lowercase();
            if ln == "const" || ln == "intercept" {
                Some(i)
            } else {
                None
            }
        })
        .collect();
    for j in 0..k {
        if X.column(j).iter().all(|&v| (v - X[(0, j)]).abs() < 1e-8_f32) {
            if !intercept_indices.contains(&j) {
                intercept_indices.push(j);
                exog_names[j] = "Intercept".to_string();
            }
        }
    }

    let is_discrete: Vec<usize> = (0..k)
        .filter(|&j| {
            if intercept_indices.contains(&j) {
                false
            } else {
                X.column(j).iter().all(|&v| v == 0.0 || v == 1.0)
            }
        })
        .collect();

    let mut sum_ame = vec![0.0_f32; k];
    let mut partial_jl_sums = vec![0.0_f32; k * k];

    let mut idx_start = 0;
    while idx_start < n {
        let idx_end = (idx_start + chunk).min(n);
        let x_chunk = X.slice(ndarray::s![idx_start..idx_end, ..]);
        let z_chunk = x_chunk.dot(&beta);
        let phi_vals = z_chunk.mapv(|z| pdf_fn(z));

        for &j in &is_discrete {
            if intercept_indices.contains(&j) {
                continue;
            }
            let xj_col = x_chunk.column(j);
            let beta_j = beta[j];
            let delta_j1 = xj_col.mapv(|x| if x == 0.0 { beta_j } else { 0.0 });
            let delta_j0 = xj_col.mapv(|x| if x == 1.0 { -beta_j } else { 0.0 });
            let z_j1 = &z_chunk + &delta_j1;
            let z_j0 = &z_chunk + &delta_j0;
            let cdf_diff_sum = z_j1.mapv(|z| cdf_fn(z)).sum()
                - z_j0.mapv(|z| cdf_fn(z)).sum();
            sum_ame[j] += cdf_diff_sum;

            let pdf_j1 = z_j1.mapv(|z| pdf_fn(z));
            let pdf_j0 = z_j0.mapv(|z| pdf_fn(z));
            for l in 0..k {
                let xl_col = x_chunk.column(l);
                let grad = if l == j {
                    pdf_j1.sum()
                } else {
                    (&pdf_j1 - &pdf_j0).dot(&xl_col)
                };
                partial_jl_sums[j * k + l] += grad;
            }
        }

        for j in 0..k {
            if intercept_indices.contains(&j) || is_discrete.contains(&j) {
                continue;
            }
            let beta_j = beta[j];
            sum_ame[j] += beta_j * phi_vals.sum();
            for l in 0..k {
                let grad = if j == l {
                    phi_vals.sum()
                } else {
                    -beta_j * (z_chunk.clone() * &x_chunk.column(l)).dot(&phi_vals)
                };
                partial_jl_sums[j * k + l] += grad;
            }
        }
        idx_start = idx_end;
    }

    let ame: Vec<f32> = sum_ame.iter().map(|v| v / n as f32).collect();
    let mut grad_ame = Array2::zeros((k, k));
    for j in 0..k {
        for l in 0..k {
            grad_ame[(j, l)] = partial_jl_sums[j * k + l] / n as f32;
        }
    }
    let cov_ame = grad_ame.dot(&cov_beta).dot(&grad_ame.t());
    let var_ame: Vec<f32> = cov_ame.diag().iter().map(|&v| v.max(0.0)).collect();
    let se_ame: Vec<f32> = var_ame.iter().map(|v| v.sqrt()).collect();

    let (mut dy_dx, mut se_err, mut z_vals, mut p_vals, mut sig, mut names) =
        (Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new(), Vec::new());
    for j in 0..k {
        if intercept_indices.contains(&j) {
            continue;
        }
        dy_dx.push(ame[j]);
        se_err.push(se_ame[j]);
        let z = if se_ame[j] > 0.0 {
            ame[j] / se_ame[j]
        } else {
            f32::NAN
        };
        z_vals.push(z);
        let p = 2.0 * (1.0 - cdf_fn(z.abs()));
        p_vals.push(p);
        sig.push(add_significance_stars(p));
        names.push(exog_names[j].clone());
    }

    let pd = py.import("pandas")?;
    let data = PyDict::new(py);
    data.set_item("dy/dx", dy_dx)?;
    data.set_item("Std. Err", se_err)?;
    data.set_item("z", z_vals)?;
    data.set_item("Pr(>|z|)", p_vals)?;
    data.set_item("Significance", sig)?;

    let kwargs = PyDict::new(py);
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
    m.add_function(wrap_pyfunction!(fit_logit, m)?)?;
    m.add_function(wrap_pyfunction!(ame, m)?)?;
    Ok(())
}
