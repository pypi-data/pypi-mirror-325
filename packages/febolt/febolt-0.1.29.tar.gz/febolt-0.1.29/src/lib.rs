// src/lib.rs
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use pyo3::types::{PyAny, PyDict};
use pyo3::exceptions::{PyValueError, PyTypeError};
use numpy::{PyArray1, PyArray2, PyArrayDyn};
use ndarray::{Array1, Array2, ArrayView1, ArrayView2, Axis};
use blas::{sger, dger};
use ndarray_linalg::{Solve, Inverse};
use std::collections::HashMap;

// ----------------------------------------------------------------------------
// A) Converter Functions (Py -> Rust ndarray), with shape fix so (i,j) indexing
// ----------------------------------------------------------------------------

// We prefix `_py` if we don't need the variable to avoid warnings about "unused variable".
fn convert_any_to_f32_2d<'py>(_py: Python<'py>, obj: &PyAny) -> PyResult<Array2<f32>> {
    let shape: Vec<usize> = obj.getattr("shape")?.extract()?;
    if shape.len() != 2 {
        return Err(PyValueError::new_err("Expected a 2D array for f32"));
    }
    let (nrows, ncols) = (shape[0], shape[1]);
    let dtype_str = obj.getattr("dtype")?.str()?.to_str()?;

    if dtype_str.contains("float32") {
        let arr_2d = obj.downcast::<PyArray2<f32>>()?;
        let view = unsafe { arr_2d.as_array() };
        Ok(view.to_owned())
    } else if dtype_str.contains("float64") {
        let arr_dyn = obj.downcast::<PyArrayDyn<f64>>()?;
        let view_dyn = unsafe { arr_dyn.as_array() };
        if view_dyn.ndim() != 2 {
            return Err(PyValueError::new_err("Expected 2D float64->f32"));
        }
        // shape fix
        let view_2d = view_dyn
            .into_shape((nrows, ncols))
            .map_err(|_| PyValueError::new_err("into_shape fail float64->f32"))?;
        let mut out = Array2::<f32>::zeros((nrows, ncols));
        for i in 0..nrows {
            for j in 0..ncols {
                out[(i, j)] = view_2d[(i, j)] as f32;
            }
        }
        Ok(out)
    } else if dtype_str.contains("int64") {
        let arr_dyn = obj.downcast::<PyArrayDyn<i64>>()?;
        let view_dyn = unsafe { arr_dyn.as_array() };
        if view_dyn.ndim() != 2 {
            return Err(PyValueError::new_err("Expected 2D int64->f32"));
        }
        let view_2d = view_dyn
            .into_shape((nrows, ncols))
            .map_err(|_| PyValueError::new_err("into_shape fail int64->f32"))?;
        let mut out = Array2::<f32>::zeros((nrows, ncols));
        for i in 0..nrows {
            for j in 0..ncols {
                out[(i, j)] = view_2d[(i, j)] as f32;
            }
        }
        Ok(out)
    } else if dtype_str.contains("int32") {
        let arr_dyn = obj.downcast::<PyArrayDyn<i32>>()?;
        let view_dyn = unsafe { arr_dyn.as_array() };
        if view_dyn.ndim() != 2 {
            return Err(PyValueError::new_err("Expected 2D int32->f32"));
        }
        let view_2d= view_dyn
            .into_shape((nrows, ncols))
            .map_err(|_| PyValueError::new_err("into_shape fail int32->f32"))?;
        let mut out= Array2::<f32>::zeros((nrows,ncols));
        for i in 0..nrows {
            for j in 0..ncols {
                out[(i,j)] = view_2d[(i,j)] as f32;
            }
        }
        Ok(out)
    } else {
        Err(PyTypeError::new_err("Unsupported 2D dtype for f32"))
    }
}

fn convert_any_to_f32_1d<'py>(_py: Python<'py>, obj: &PyAny) -> PyResult<Array1<f32>> {
    let shape: Vec<usize> = obj.getattr("shape")?.extract()?;
    if shape.len() == 2 && shape[1] == 1 {
        let flattened = obj.call_method0("flatten")?;
        return convert_any_to_f32_1d(_py, flattened);
    } else if shape.len() != 1 {
        return Err(PyValueError::new_err("Expected 1D array for f32"));
    }
    let dtype_str= obj.getattr("dtype")?.str()?.to_str()?;
    if dtype_str.contains("float32") {
        let arr_1d= obj.downcast::<PyArray1<f32>>()?;
        let view= unsafe { arr_1d.as_array() };
        Ok(view.to_owned())
    } else if dtype_str.contains("float64") {
        let arr_dyn= obj.downcast::<PyArrayDyn<f64>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=1 {
            return Err(PyValueError::new_err("Expected 1D float64->f32"));
        }
        let mut out= Array1::<f32>::zeros(view_dyn.len());
        for i in 0..view_dyn.len() {
            out[i] = view_dyn[i] as f32;
        }
        Ok(out)
    } else if dtype_str.contains("int64") {
        let arr_dyn= obj.downcast::<PyArrayDyn<i64>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=1 {
            return Err(PyValueError::new_err("Expected 1D int64->f32"));
        }
        let mut out= Array1::<f32>::zeros(view_dyn.len());
        for i in 0..view_dyn.len() {
            out[i] = view_dyn[i] as f32;
        }
        Ok(out)
    } else if dtype_str.contains("int32") {
        let arr_dyn= obj.downcast::<PyArrayDyn<i32>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=1 {
            return Err(PyValueError::new_err("Expected 1D int32->f32"));
        }
        let mut out= Array1::<f32>::zeros(view_dyn.len());
        for i in 0..view_dyn.len() {
            out[i] = view_dyn[i] as f32;
        }
        Ok(out)
    } else {
        Err(PyTypeError::new_err("Unsupported dtype for f32 1D"))
    }
}

fn convert_any_to_f64_2d<'py>(_py: Python<'py>, obj: &PyAny) -> PyResult<Array2<f64>> {
    let shape: Vec<usize> = obj.getattr("shape")?.extract()?;
    if shape.len()!=2 {
        return Err(PyValueError::new_err("Expected a 2D array for f64"));
    }
    let (nrows,ncols)= (shape[0], shape[1]);
    let dtype_str= obj.getattr("dtype")?.str()?.to_str()?;

    if dtype_str.contains("float64") {
        let arr_2d= obj.downcast::<PyArray2<f64>>()?;
        let view= unsafe { arr_2d.as_array() };
        Ok(view.to_owned())
    } else if dtype_str.contains("float32") {
        let arr_dyn= obj.downcast::<PyArrayDyn<f32>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=2 {
            return Err(PyValueError::new_err("Expected 2D float32->f64"));
        }
        let view_2d= view_dyn
            .into_shape((nrows,ncols))
            .map_err(|_| PyValueError::new_err("into_shape fail float32->f64"))?;
        let mut out= Array2::<f64>::zeros((nrows,ncols));
        for i in 0..nrows {
            for j in 0..ncols {
                out[(i,j)] = view_2d[(i,j)] as f64;
            }
        }
        Ok(out)
    } else if dtype_str.contains("int64") {
        let arr_dyn= obj.downcast::<PyArrayDyn<i64>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=2 {
            return Err(PyValueError::new_err("Expected 2D int64->f64"));
        }
        let view_2d= view_dyn
            .into_shape((nrows,ncols))
            .map_err(|_| PyValueError::new_err("into_shape fail int64->f64"))?;
        let mut out= Array2::<f64>::zeros((nrows,ncols));
        for i in 0..nrows {
            for j in 0..ncols {
                out[(i,j)] = view_2d[(i,j)] as f64;
            }
        }
        Ok(out)
    } else if dtype_str.contains("int32") {
        let arr_dyn= obj.downcast::<PyArrayDyn<i32>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=2 {
            return Err(PyValueError::new_err("Expected 2D int32->f64"));
        }
        let view_2d= view_dyn
            .into_shape((nrows,ncols))
            .map_err(|_| PyValueError::new_err("into_shape fail int32->f64"))?;
        let mut out= Array2::<f64>::zeros((nrows,ncols));
        for i in 0..nrows {
            for j in 0..ncols {
                out[(i,j)] = view_2d[(i,j)] as f64;
            }
        }
        Ok(out)
    } else {
        Err(PyTypeError::new_err("Unsupported dtype for f64 2D"))
    }
}

fn convert_any_to_f64_1d<'py>(_py: Python<'py>, obj: &PyAny)-> PyResult<Array1<f64>> {
    let shape: Vec<usize>= obj.getattr("shape")?.extract()?;
    if shape.len()==2 && shape[1]==1 {
        let flattened= obj.call_method0("flatten")?;
        return convert_any_to_f64_1d(_py, flattened);
    } else if shape.len()!=1 {
        return Err(PyValueError::new_err("Expected 1D array for f64"));
    }
    let dtype_str= obj.getattr("dtype")?.str()?.to_str()?;
    if dtype_str.contains("float64") {
        let arr_1d= obj.downcast::<PyArray1<f64>>()?;
        let view= unsafe { arr_1d.as_array() };
        Ok(view.to_owned())
    } else if dtype_str.contains("float32") {
        let arr_dyn= obj.downcast::<PyArrayDyn<f32>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=1 {
            return Err(PyValueError::new_err("Expected 1D float32->f64"));
        }
        let mut out= Array1::<f64>::zeros(view_dyn.len());
        for i in 0..view_dyn.len() {
            out[i]= view_dyn[i] as f64;
        }
        Ok(out)
    } else if dtype_str.contains("int64") {
        let arr_dyn= obj.downcast::<PyArrayDyn<i64>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=1 {
            return Err(PyValueError::new_err("Expected 1D int64->f64"));
        }
        let mut out= Array1::<f64>::zeros(view_dyn.len());
        for i in 0..view_dyn.len() {
            out[i]= view_dyn[i] as f64;
        }
        Ok(out)
    } else if dtype_str.contains("int32") {
        let arr_dyn= obj.downcast::<PyArrayDyn<i32>>()?;
        let view_dyn= unsafe { arr_dyn.as_array() };
        if view_dyn.ndim()!=1 {
            return Err(PyValueError::new_err("Expected 1D int32->f64"));
        }
        let mut out= Array1::<f64>::zeros(view_dyn.len());
        for i in 0..view_dyn.len() {
            out[i]= view_dyn[i] as f64;
        }
        Ok(out)
    } else {
        Err(PyTypeError::new_err("Unsupported dtype for f64 1D"))
    }
}

//
// ===========================================================================
// B) Single-Precision + Double-Precision modules
// ===========================================================================
mod probit_f32 {
    use super::*;
    use std::f32::consts::{PI, SQRT_2};

    #[inline]
    pub fn erf32(x: f32)-> f32 {
        let a1=0.254829592_f32; 
        let a2=-0.284496736_f32; 
        let a3=1.421413741_f32; 
        let a4=-1.453152027_f32; 
        let a5=1.061405429_f32; 
        let p=0.3275911_f32;
        let sign= if x<0.0{-1.0}else{1.0};
        let x= x.abs();
        let t=1.0/(1.0+ p*x);
        let y=1.0- ((((a5*t+a4)*t+a3)*t+a2)*t+a1)*t* (-x*x).exp();
        sign*y
    }
    #[inline]
    pub fn pdf32(z: f32)-> f32 {
        (-0.5*z*z).exp() / (2.0* PI).sqrt()
    }
    #[inline]
    pub fn cdf32(z: f32)-> f32 {
        let val= 0.5*(1.0+ erf32(z/ SQRT_2));
        val.max(1e-15).min(1.0- 1e-15)
    }

    pub struct ProbitF32<'a> {
        pub endog: ArrayView1<'a,f32>,
        pub exog: ArrayView2<'a,f32>,
        pub weights: Option<ArrayView1<'a,f32>>,
    }

    impl<'a> ProbitF32<'a> {
        // <-- Add the 'new' constructor explicitly:
        pub fn new(
            endog: ArrayView1<'a,f32>,
            exog: ArrayView2<'a,f32>,
            weights: Option<ArrayView1<'a,f32>>,
        ) -> Self {
            ProbitF32 { endog, exog, weights }
        }

        fn w(&self, i: usize)-> f32 {
            self.weights.map(|w| w[i]).unwrap_or(1.0)
        }
        pub fn xbeta(&self, params: &ArrayView1<f32>, out: &mut Array1<f32>) {
            *out= self.exog.dot(params);
        }
        pub fn loglike(&self, xbeta: &ArrayView1<f32>)-> f32 {
            let q= self.endog.mapv(|y|2.0*y-1.0);
            let mut sum=0.0;
            for i in 0..xbeta.len() {
                let z= q[i]*xbeta[i];
                let val= cdf32(z).ln();
                sum += self.w(i)* val;
            }
            sum
        }
        pub fn score(&self, xbeta: &ArrayView1<f32>, grad_out: &mut Array1<f32>) {
            grad_out.fill(0.0);
            let n= self.exog.nrows();
            let k= self.exog.ncols();
            let q= self.endog.mapv(|y|2.0*y-1.0);
            for j in 0..k {
                let mut sum_j=0.0;
                let col_j= self.exog.column(j);
                for i in 0..n {
                    let z= q[i]*xbeta[i];
                    let pdfv= pdf32(z);
                    let cdfv= cdf32(z);
                    let ratio= pdfv/cdfv;
                    let factor= ratio*q[i]* self.w(i);
                    sum_j += col_j[i]* factor;
                }
                grad_out[j]= sum_j;
            }
        }
        pub fn hessian(&self, xbeta: &ArrayView1<f32>, hess_out: &mut Array2<f32>) {
            hess_out.fill(0.0);
            let (n,k)= self.exog.dim();
            let q= self.endog.mapv(|y| 2.0*y-1.0);
            let mut Xw= self.exog.to_owned();
            for i in 0..n {
                let z= q[i]*xbeta[i];
                let pdfv= pdf32(z);
                let cdfv= cdf32(z);
                let ratio= pdfv/cdfv;
                let w_i= (ratio*ratio + ratio*z)* self.w(i);
                let sqrt_w= w_i.sqrt();
                for j in 0..k {
                    Xw[(i,j)]*= sqrt_w;
                }
            }
            let tmp= Xw.t().dot(&Xw);
            *hess_out= tmp.mapv(|val| -val);
        }
        pub fn fit_naive_newton(&self, max_iter: usize, tol: f32)-> (Array1<f32>, f32, bool, usize){
            let k= self.exog.ncols();
            let mut params= Array1::<f32>::zeros(k);
            let mut xbeta= Array1::<f32>::zeros(self.exog.nrows());
            let mut grad= Array1::<f32>::zeros(k);
            let mut hess= Array2::<f32>::zeros((k,k));
            self.xbeta(&params.view(), &mut xbeta);
            let mut ll_old= self.loglike(&xbeta.view());
            let mut converged= false;
            let mut iter_used=0;
            for iter in 0..max_iter {
                iter_used= iter;
                self.score(&xbeta.view(), &mut grad);
                self.hessian(&xbeta.view(), &mut hess);
                let step= match hess.solve(&grad){
                    Ok(s)=> s,
                    Err(_)=>{
                        eprintln!("Hessian singular f32 at iter {}", iter);
                        break;
                    }
                };
                for j in 0..k {
                    params[j] -= step[j];
                }
                self.xbeta(&params.view(), &mut xbeta);
                let ll_new= self.loglike(&xbeta.view());
                if (ll_new- ll_old).abs()< tol {
                    converged=true;
                    ll_old= ll_new;
                    break;
                }
                ll_old= ll_new;
            }
            (params, ll_old, converged, iter_used)
        }
    }

    pub fn robust_cov_sger_f32(
        exog: &ArrayView2<f32>,
        xbeta: &ArrayView1<f32>,
        endog: &ArrayView1<f32>,
        weights: Option<&ArrayView1<f32>>,
        h_inv: &ArrayView2<f32>,
        cluster: Option<ArrayView2<f32>>,
    )-> Array2<f32> {
        let nobs= exog.nrows();
        let kvars= exog.ncols();
        let q= endog.mapv(|y|2.0*y-1.0);
        let z= &q * xbeta;
        let mut M_flat= vec![0.0_f32; kvars*kvars];

        if let Some(cluster_mat)= cluster {
            if cluster_mat.ncols()!=1 {
                // White style => sger each row
                for i in 0..nobs {
                    let pdf= pdf32(z[i]);
                    let cdf= cdf32(z[i]);
                    let ratio= pdf/cdf;
                    let w_i= weights.map(|ww| ww[i]).unwrap_or(1.0);
                    let factor= ratio*q[i]* w_i;
                    let row_vec= exog.row(i);
                    let alpha= factor;
                    let incx=1;
                    let incy=1;
                    let lda= kvars as i32;
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
                            lda
                        );
                    }
                }
            } else {
                // single cluster col
                let mut cluster_map: HashMap<u32,Vec<f32>>= HashMap::new();
                for i in 0..nobs {
                    let cval= cluster_mat[[i,0]];
                    let key= cval.to_bits();
                    let pdf= pdf32(z[i]);
                    let cdf= cdf32(z[i]);
                    let ratio= pdf/cdf;
                    let w_i= weights.map(|ww| ww[i]).unwrap_or(1.0);
                    let factor= ratio*q[i]* w_i;
                    let row_vec= exog.row(i);
                    let entry= cluster_map.entry(key).or_insert_with(|| vec![0.0_f32; kvars]);
                    for j in 0..kvars {
                        entry[j]+= row_vec[j]*factor;
                    }
                }
                for sc_vec in cluster_map.values() {
                    let alpha= 1.0_f32;
                    let incx=1;
                    let incy=1;
                    let lda= kvars as i32;
                    unsafe {
                        sger(
                            kvars as i32,
                            kvars as i32,
                            alpha,
                            sc_vec,
                            incx,
                            sc_vec,
                            incy,
                            &mut M_flat,
                            lda
                        );
                    }
                }
            }
        } else {
            // White
            for i in 0..nobs {
                let pdf= pdf32(z[i]);
                let cdf= cdf32(z[i]);
                let ratio= pdf/cdf;
                let w_i= weights.map(|ww| ww[i]).unwrap_or(1.0);
                let factor= ratio*q[i]* w_i;
                let row_vec= exog.row(i);
                let alpha= factor;
                let incx=1;
                let incy=1;
                let lda= kvars as i32;
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
                        lda
                    );
                }
            }
        }

        let M = Array2::from_shape_vec((kvars, kvars), M_flat)
            .unwrap()
            .reversed_axes();
        h_inv.dot(&M).dot(h_inv)
    }
}


mod probit_f64 {
    use super::*;
    use std::f64::consts::{PI, SQRT_2};

    #[inline]
    pub fn erf64(x: f64)-> f64 {
        let a1=0.254829592_f64; 
        let a2=-0.284496736_f64; 
        let a3=1.421413741_f64; 
        let a4=-1.453152027_f64; 
        let a5=1.061405429_f64; 
        let p=0.3275911_f64;
        let sign= if x<0.0{-1.0}else{1.0};
        let x= x.abs();
        let t=1.0/(1.0+ p*x);
        let y=1.0- ((((a5*t+a4)*t+a3)*t+a2)*t+a1)*t* (-x*x).exp();
        sign*y
    }
    #[inline]
    pub fn pdf64(z: f64)-> f64 {
        (-0.5*z*z).exp() / (2.0* PI).sqrt()
    }
    #[inline]
    pub fn cdf64(z: f64)-> f64 {
        let val= 0.5*(1.0+ erf64(z/ SQRT_2));
        val.max(1e-15).min(1.0- 1e-15)
    }

    pub struct ProbitF64<'a> {
        pub endog: ArrayView1<'a,f64>,
        pub exog: ArrayView2<'a,f64>,
        pub weights: Option<ArrayView1<'a,f64>>,
    }

    impl<'a> ProbitF64<'a> {
        // Add the new constructor
        pub fn new(
            endog: ArrayView1<'a,f64>,
            exog: ArrayView2<'a,f64>,
            weights: Option<ArrayView1<'a,f64>>,
        ) -> Self {
            ProbitF64 { endog, exog, weights }
        }

        fn w(&self, i: usize)-> f64 {
            self.weights.map(|ww| ww[i]).unwrap_or(1.0)
        }
        pub fn xbeta(&self, params: &ArrayView1<f64>, out: &mut Array1<f64>) {
            *out= self.exog.dot(params);
        }
        pub fn loglike(&self, xbeta: &ArrayView1<f64>)-> f64 {
            let q= self.endog.mapv(|y|2.0*y-1.0);
            let mut sum=0.0;
            for i in 0..xbeta.len() {
                let z= q[i]* xbeta[i];
                sum += self.w(i)* cdf64(z).ln();
            }
            sum
        }
        pub fn score(&self, xbeta: &ArrayView1<f64>, grad_out: &mut Array1<f64>) {
            grad_out.fill(0.0);
            let n= self.exog.nrows();
            let k= self.exog.ncols();
            let q= self.endog.mapv(|y|2.0*y-1.0);
            for j in 0..k {
                let col_j= self.exog.column(j);
                let mut sum_j=0.0;
                for i in 0..n {
                    let z= q[i]* xbeta[i];
                    let pdfv= pdf64(z);
                    let cdfv= cdf64(z);
                    let ratio= pdfv/cdfv;
                    let factor= ratio*q[i]* self.w(i);
                    sum_j += col_j[i]* factor;
                }
                grad_out[j]= sum_j;
            }
        }
        pub fn hessian(&self, xbeta: &ArrayView1<f64>, hess_out: &mut Array2<f64>) {
            hess_out.fill(0.0);
            let (n,k)= self.exog.dim();
            let q= self.endog.mapv(|y|2.0*y-1.0);
            let mut Xw= self.exog.to_owned();
            for i in 0..n {
                let z= q[i]* xbeta[i];
                let pdfv= pdf64(z);
                let cdfv= cdf64(z);
                let ratio= pdfv/cdfv;
                let w_i= (ratio* ratio + ratio*z)* self.w(i);
                let sqrt_w= w_i.sqrt();
                for j in 0..k {
                    Xw[(i,j)]*= sqrt_w;
                }
            }
            let tmp= Xw.t().dot(&Xw);
            *hess_out= tmp.mapv(|v| -v);
        }
        pub fn fit_naive_newton(&self, max_iter: usize, tol: f64)->(Array1<f64>, f64, bool, usize){
            let k= self.exog.ncols();
            let mut params= Array1::<f64>::zeros(k);
            let mut xbeta= Array1::<f64>::zeros(self.exog.nrows());
            let mut grad= Array1::<f64>::zeros(k);
            let mut hess= Array2::<f64>::zeros((k,k));
            self.xbeta(&params.view(), &mut xbeta);
            let mut ll_old= self.loglike(&xbeta.view());
            let mut converged= false;
            let mut iter_used=0;
            for iter in 0..max_iter {
                iter_used=iter;
                self.score(&xbeta.view(), &mut grad);
                self.hessian(&xbeta.view(), &mut hess);
                let step= match hess.solve(&grad){
                    Ok(s)=> s,
                    Err(_)=>{
                        eprintln!("Hessian singular f64 iter {}", iter);
                        break;
                    }
                };
                for j in 0..k {
                    params[j] -= step[j];
                }
                self.xbeta(&params.view(), &mut xbeta);
                let ll_new= self.loglike(&xbeta.view());
                if (ll_new- ll_old).abs()< tol {
                    converged= true;
                    ll_old= ll_new;
                    break;
                }
                ll_old= ll_new;
            }
            (params, ll_old, converged, iter_used)
        }
    }

    pub fn robust_cov_dger_f64(
        exog: &ArrayView2<f64>,
        xbeta: &ArrayView1<f64>,
        endog: &ArrayView1<f64>,
        weights: Option<&ArrayView1<f64>>,
        h_inv: &ArrayView2<f64>,
        cluster: Option<ArrayView2<f64>>,
    )-> Array2<f64> {
        let nobs= exog.nrows();
        let kvars= exog.ncols();
        let q= endog.mapv(|y|2.0*y-1.0);
        let z= &q* xbeta;
        let mut M_flat= vec![0.0_f64; kvars*kvars];

        if let Some(cluster_mat)= cluster {
            if cluster_mat.ncols()!=1 {
                // White => dger each row
                for i in 0..nobs {
                    let pdfv= pdf64(z[i]);
                    let cdfv= cdf64(z[i]);
                    let ratio= pdfv/cdfv;
                    let w_i= weights.map(|ww|ww[i]).unwrap_or(1.0);
                    let factor= ratio*q[i]* w_i;
                    let row_vec= exog.row(i);
                    let alpha= factor;
                    let incx=1;
                    let incy=1;
                    let lda= kvars as i32;
                    unsafe {
                        dger(
                            kvars as i32,
                            kvars as i32,
                            alpha,
                            row_vec.as_slice().unwrap(),
                            incx,
                            row_vec.as_slice().unwrap(),
                            incy,
                            &mut M_flat,
                            lda
                        );
                    }
                }
            } else {
                // single cluster col
                let mut cluster_map: HashMap<u64,Vec<f64>>= HashMap::new();
                for i in 0..nobs {
                    let cval= cluster_mat[[i,0]];
                    let key= cval.to_bits();
                    let pdfv= pdf64(z[i]);
                    let cdfv= cdf64(z[i]);
                    let ratio= pdfv/cdfv;
                    let w_i= weights.map(|ww|ww[i]).unwrap_or(1.0);
                    let factor= ratio*q[i]* w_i;
                    let row_vec= exog.row(i);
                    let entry= cluster_map.entry(key).or_insert_with(|| vec![0.0_f64; kvars]);
                    for j in 0..kvars {
                        entry[j]+= row_vec[j]* factor;
                    }
                }
                for sc_vec in cluster_map.values() {
                    let alpha= 1.0_f64;
                    let incx=1;
                    let incy=1;
                    let lda= kvars as i32;
                    unsafe {
                        dger(
                            kvars as i32,
                            kvars as i32,
                            alpha,
                            sc_vec,
                            incx,
                            sc_vec,
                            incy,
                            &mut M_flat,
                            lda
                        );
                    }
                }
            }
        } else {
            // White
            for i in 0..nobs {
                let pdfv= pdf64(z[i]);
                let cdfv= cdf64(z[i]);
                let ratio= pdfv/cdfv;
                let w_i= weights.map(|ww|ww[i]).unwrap_or(1.0);
                let factor= ratio*q[i]* w_i;
                let row_vec= exog.row(i);
                let alpha= factor;
                let incx=1;
                let incy=1;
                let lda= kvars as i32;
                unsafe {
                    dger(
                        kvars as i32,
                        kvars as i32,
                        alpha,
                        row_vec.as_slice().unwrap(),
                        incx,
                        row_vec.as_slice().unwrap(),
                        incy,
                        &mut M_flat,
                        lda
                    );
                }
            }
        }
        // Now define M
        let M= Array2::from_shape_vec((kvars,kvars), M_flat)
            .unwrap()
            .reversed_axes();
        h_inv.dot(&M).dot(h_inv)
    }
}

// ---------------------------------------------------------------------------
// D) model_fit + fit_probit + ame, with lifetime <'py>
// ---------------------------------------------------------------------------

fn model_fit_f32(
    exog: &Array2<f32>,
    endog: &Array1<f32>,
    weights: Option<&Array1<f32>>,
    max_iter: usize,
    tol: f32,
    robust: bool,
    cluster_vars: Option<&PyAny>,
) -> PyResult<(Array1<f32>, f32, bool, usize, Array2<f32>)> {
    use probit_f32::*;
    let probit = ProbitF32::new(endog.view(), exog.view(), weights.map(|w| w.view()));
    let (params, llf, converged, iters)= probit.fit_naive_newton(max_iter, tol);

    let mut xbeta= Array1::<f32>::zeros(exog.nrows());
    probit.xbeta(&params.view(), &mut xbeta);
    let mut hess= Array2::<f32>::zeros((params.len(), params.len()));
    probit.hessian(&xbeta.view(), &mut hess);

    let mut cov_final= match hess.inv() {
        Ok(inv_h)=> -inv_h,
        Err(_)=>{
            eprintln!("Hessian singular => identity f32");
            -Array2::<f32>::eye(exog.ncols())
        }
    };
    if robust {
        let cluster_view= if let Some(pyarr)= cluster_vars {
            let arr_f32= pyarr.downcast::<PyArray2<f32>>()?;
            let view= unsafe { arr_f32.as_array() };
            if view.nrows()!= exog.nrows() {
                return Err(PyValueError::new_err("cluster row mismatch f32"));
            }
            Some(view)
        } else {
            None
        };
        let h_inv= cov_final.mapv(|x| -x);

        // fix the weights Option => Option<&ArrayView1<_>>
        let w_view = weights.map(|w| w.view());
        let w_view_ref = w_view.as_ref();

        cov_final= robust_cov_sger_f32(
            &exog.view(),
            &xbeta.view(),
            &endog.view(),
            w_view_ref,
            &h_inv.view(),
            cluster_view
        );
    }

    Ok((params, llf, converged, iters, cov_final))
}

fn model_fit_f64(
    exog: &Array2<f64>,
    endog: &Array1<f64>,
    weights: Option<&Array1<f64>>,
    max_iter: usize,
    tol: f64,
    robust: bool,
    cluster_vars: Option<&PyAny>,
) -> PyResult<(Array1<f64>, f64, bool, usize, Array2<f64>)> {
    use probit_f64::*;
    let probit= ProbitF64::new(endog.view(), exog.view(), weights.map(|w| w.view()));
    let (params, llf, converged, iters)= probit.fit_naive_newton(max_iter, tol);

    let mut xbeta= Array1::<f64>::zeros(exog.nrows());
    probit.xbeta(&params.view(), &mut xbeta);
    let mut hess= Array2::<f64>::zeros((params.len(), params.len()));
    probit.hessian(&xbeta.view(), &mut hess);

    let mut cov_final= match hess.inv() {
        Ok(inv_h)=> -inv_h,
        Err(_)=>{
            eprintln!("Hessian singular => identity f64");
            -Array2::<f64>::eye(exog.ncols())
        }
    };
    if robust {
        let cluster_view= if let Some(pyarr)= cluster_vars {
            let arr_f64= pyarr.downcast::<PyArray2<f64>>()?;
            let view= unsafe { arr_f64.as_array() };
            if view.nrows()!= exog.nrows() {
                return Err(PyValueError::new_err("cluster row mismatch f64"));
            }
            Some(view)
        } else {
            None
        };
        let h_inv= cov_final.mapv(|x| -x);

        let w_view = weights.map(|w| w.view());
        let w_view_ref = w_view.as_ref();

        cov_final= robust_cov_dger_f64(
            &exog.view(),
            &xbeta.view(),
            &endog.view(),
            w_view_ref,
            &h_inv.view(),
            cluster_view
        );
    }
    Ok((params, llf, converged, iters, cov_final))
}

#[pyfunction]
fn fit_probit<'py>(
    py: Python<'py>,
    endog_py: &PyAny,
    exog_py: &PyAny,
    max_iter: Option<usize>,
    tol: Option<f32>,
    robust: Option<bool>,
    cluster_vars: Option<&PyAny>,
    intercept: Option<bool>,
    precise: Option<bool>,
    weight_var: Option<&PyAny>,
) -> PyResult<&'py PyAny> {
    let use_f64= precise.unwrap_or(false);
    if !use_f64 {
        // single
        let endog= convert_any_to_f32_1d(py, endog_py)?;
        let mut exog= convert_any_to_f32_2d(py, exog_py)?;
        let weights= if let Some(wobj)= weight_var {
            Some(convert_any_to_f32_1d(py, wobj)?)
        } else { None };

        if intercept.unwrap_or(true) {
            let nobs= exog.nrows();
            let ones= ndarray::Array2::<f32>::ones((nobs,1));
            exog= ndarray::concatenate(Axis(1), &[ones.view(), exog.view()])
                .map_err(|e| PyValueError::new_err(format!("Concat intercept f32: {}", e)))?;
        }
        let k= exog.ncols();
        let exog_names= if intercept.unwrap_or(true) {
            let mut names= vec!["Intercept".to_string()];
            for j in 0..(k-1) {
                names.push(format!("x{}", j));
            }
            names
        } else {
            (0..k).map(|j| format!("x{}", j)).collect()
        };

        let (params, llf, converged, iters, cov_final)= model_fit_f32(
            &exog,
            &endog,
            weights.as_ref(),
            max_iter.unwrap_or(30),
            tol.unwrap_or(1e-6_f32),
            robust.unwrap_or(false),
            cluster_vars
        )?;

        // We'll store them as PyArrays in a dict
        let dict= PyDict::new(py);

        let params_py= PyArray1::from_owned_array(py, params);
        let cov_py= PyArray2::from_owned_array(py, cov_final);
        let exog_py= PyArray2::from_owned_array(py, exog);
        let endog_py_= PyArray1::from_owned_array(py, endog);

        dict.set_item("params", params_py)?;
        dict.set_item("cov_params", cov_py)?;
        dict.set_item("exog_names", exog_names)?;
        dict.set_item("loglike", llf)?;
        dict.set_item("iterations", iters)?;
        dict.set_item("converged", converged)?;
        dict.set_item("exog", exog_py)?;
        dict.set_item("endog", endog_py_)?;

        Ok(dict.into())
    } else {
        // double
        let endog= convert_any_to_f64_1d(py, endog_py)?;
        let mut exog= convert_any_to_f64_2d(py, exog_py)?;
        let weights= if let Some(wobj)= weight_var {
            Some(convert_any_to_f64_1d(py, wobj)?)
        } else { None };

        if intercept.unwrap_or(true) {
            let nobs= exog.nrows();
            let ones= ndarray::Array2::<f64>::ones((nobs,1));
            exog= ndarray::concatenate(Axis(1), &[ones.view(), exog.view()])
                .map_err(|e| PyValueError::new_err(format!("Concat intercept f64: {}", e)))?;
        }
        let k= exog.ncols();
        let exog_names= if intercept.unwrap_or(true) {
            let mut names= vec!["Intercept".to_string()];
            for j in 0..(k-1){
                names.push(format!("x{}", j));
            }
            names
        } else {
            (0..k).map(|j| format!("x{}", j)).collect()
        };

        let (params, llf, converged, iters, cov_final)= model_fit_f64(
            &exog,
            &endog,
            weights.as_ref(),
            max_iter.unwrap_or(30),
            tol.map(|x| x as f64).unwrap_or(1e-6_f64),
            robust.unwrap_or(false),
            cluster_vars
        )?;

        let dict= PyDict::new(py);

        let params_py= PyArray1::from_owned_array(py, params);
        let cov_py= PyArray2::from_owned_array(py, cov_final);
        let exog_py= PyArray2::from_owned_array(py, exog);
        let endog_py_= PyArray1::from_owned_array(py, endog);

        dict.set_item("params", params_py)?;
        dict.set_item("cov_params", cov_py)?;
        dict.set_item("exog_names", exog_names)?;
        dict.set_item("loglike", llf)?;
        dict.set_item("iterations", iters)?;
        dict.set_item("converged", converged)?;
        dict.set_item("exog", exog_py)?;
        dict.set_item("endog", endog_py_)?;

        Ok(dict.into())
    }
}

#[pyfunction]
fn ame<'py>(
    py: Python<'py>,
    probit_model: &PyAny,
    precise: Option<bool>,
) -> PyResult<&'py PyAny> {
    let use_f64= precise.unwrap_or(false);
    if !use_f64 {
        ame_f32(py, probit_model)
    } else {
        ame_f64(py, probit_model)
    }
}

// Single-precision AME
fn ame_f32<'py>(py: Python<'py>, probit_model: &PyAny) -> PyResult<&'py PyAny> {
    use probit_f32::{cdf32, pdf32};

    let params_py= probit_model.get_item("params")?;
    let params_nd= params_py.downcast::<PyArray1<f32>>()?;
    let params_arr= unsafe { params_nd.as_array() }.to_owned();

    let cov_py= probit_model.get_item("cov_params")?;
    let cov_nd= cov_py.downcast::<PyArray2<f32>>()?;
    let cov_arr= unsafe { cov_nd.as_array() }.to_owned();

    let exog_names: Vec<String>= probit_model.get_item("exog_names")?.extract()?;
    let exog_py= probit_model.get_item("exog")?.downcast::<PyArray2<f32>>()?;
    let exog_arr= unsafe { exog_py.as_array() };
    let (n,k)= exog_arr.dim();

    // intercept detection
    let mut intercept_indices= vec![];
    for (ix,name) in exog_names.iter().enumerate() {
        let lower= name.to_lowercase();
        if lower=="intercept" || lower=="const" {
            intercept_indices.push(ix);
        }
    }
    for j in 0..k {
        let col_j= exog_arr.column(j);
        let first_val= col_j[0];
        let all_same= col_j.iter().all(|&v| (v-first_val).abs()<1e-12);
        if all_same && !intercept_indices.contains(&j) {
            intercept_indices.push(j);
        }
    }
    // discrete columns
    let is_discrete: Vec<usize> = (0..k).filter(|&jj|{
        if intercept_indices.contains(&jj){ false }
        else {
            let col_j= exog_arr.column(jj);
            col_j.iter().all(|&v| v==0.0 || v==1.0)
        }
    }).collect();

    let z_full= exog_arr.dot(&params_arr);
    let phi_vals= z_full.mapv(|z| pdf32(z));

    let mut sum_ame= vec![0.0_f32; k];
    let mut partial_jl_sums= vec![0.0_f32; k*k];

    // discrete
    for &j in &is_discrete {
        if intercept_indices.contains(&j){ continue; }
        let beta_j= params_arr[j];
        let col_j= exog_arr.column(j);
        let delta_j1= col_j.mapv(|x| if x==0.0 {beta_j}else{0.0});
        let delta_j0= col_j.mapv(|x| if x==1.0 {-beta_j}else{0.0});
        let z_j1= &z_full+ &delta_j1;
        let z_j0= &z_full+ &delta_j0;
        let cdf_j1= z_j1.mapv(|z| cdf32(z));
        let cdf_j0= z_j0.mapv(|z| cdf32(z));
        sum_ame[j]+= cdf_j1.sum() - cdf_j0.sum();

        let pdf_j1= z_j1.mapv(|z| pdf32(z));
        let pdf_j0= z_j0.mapv(|z| pdf32(z));
        let diff_pdf= &pdf_j1 - &pdf_j0;
        for l in 0..k {
            if l== j {
                partial_jl_sums[j*k + l]+= pdf_j1.sum();
            } else {
                partial_jl_sums[j*k + l]+= diff_pdf.dot(&exog_arr.column(l));
            }
        }
    }

    // continuous
    for j in 0..k {
        if intercept_indices.contains(&j) || is_discrete.contains(&j){
            continue;
        }
        let beta_j= params_arr[j];
        let sum_phi= phi_vals.sum();
        sum_ame[j]+= beta_j* sum_phi;

        let pprime= &z_full* &phi_vals* -1.0_f32;
        let mut M= exog_arr.to_owned();
        for (i, mut row_i) in M.outer_iter_mut().enumerate() {
            row_i.mapv_inplace(|val| val* pprime[i]);
        }
        let col_sums= M.sum_axis(Axis(0));
        for l in 0..k {
            let mut val= beta_j* col_sums[l];
            if l== j {
                val+= sum_phi;
            }
            partial_jl_sums[j*k + l]+= val;
        }
    }

    let ame: Vec<f32>= sum_ame.iter().map(|v| *v/(n as f32)).collect();
    let mut grad_ame= Array2::<f32>::zeros((k,k));
    for j in 0..k {
        for l in 0..k {
            grad_ame[(j,l)] = partial_jl_sums[j*k + l]/(n as f32);
        }
    }
    let cov_ame= grad_ame.dot(&cov_arr).dot(&grad_ame.t());
    let var_ame= cov_ame.diag().mapv(|v| v.max(0.0));
    let se_ame= var_ame.mapv(|v| v.sqrt());

    let add_stars= |p:f32|-> &'static str {
        if p<0.01 {"***"}
        else if p<0.05 {"**"}
        else if p<0.1 {"*"}
        else {""}
    };
    let mut dy_dx= vec![];
    let mut se_err= vec![];
    let mut z_vals= vec![];
    let mut p_vals= vec![];
    let mut sig= vec![];
    let mut names= vec![];

    for j in 0..k {
        if intercept_indices.contains(&j) { continue; }
        let val= ame[j];
        let se= se_ame[j];
        let z= if se>0.0 { val/se } else { f32::NAN };
        let p= 2.0*(1.0- cdf32(z.abs()));
        dy_dx.push(val);
        se_err.push(se);
        z_vals.push(z);
        p_vals.push(p);
        sig.push(add_stars(p));
        names.push(exog_names[j].clone());
    }

    let pd= py.import("pandas")?;
    let data= PyDict::new(py);
    data.set_item("dy/dx", dy_dx)?;
    data.set_item("Std. Err", se_err)?;
    data.set_item("z", z_vals)?;
    data.set_item("Pr(>|z|)", p_vals)?;
    data.set_item("Significance", sig)?;

    let kwargs= PyDict::new(py);
    kwargs.set_item("data", data)?;
    kwargs.set_item("index", names)?;

    Ok(pd.call_method("DataFrame", (), Some(kwargs))?)
}

fn ame_f64<'py>(py: Python<'py>, probit_model: &PyAny) -> PyResult<&'py PyAny> {
    use probit_f64::{cdf64, pdf64};

    let params_py= probit_model.get_item("params")?;
    let params_nd= params_py.downcast::<PyArray1<f64>>()?;
    let params_arr= unsafe { params_nd.as_array() }.to_owned();

    let cov_py= probit_model.get_item("cov_params")?;
    let cov_nd= cov_py.downcast::<PyArray2<f64>>()?;
    let cov_arr= unsafe { cov_nd.as_array() }.to_owned();

    let exog_names: Vec<String>= probit_model.get_item("exog_names")?.extract()?;
    let exog_py= probit_model.get_item("exog")?.downcast::<PyArray2<f64>>()?;
    let exog_arr= unsafe { exog_py.as_array() };
    let (n,k)= exog_arr.dim();

    // intercept detection
    let mut intercept_indices= vec![];
    for (ix,nm) in exog_names.iter().enumerate() {
        let lower= nm.to_lowercase();
        if lower=="intercept"|| lower=="const" {
            intercept_indices.push(ix);
        }
    }
    for j in 0..k {
        let col_j= exog_arr.column(j);
        let first_val= col_j[0];
        let all_same= col_j.iter().all(|&v| (v-first_val).abs()<1e-12);
        if all_same && !intercept_indices.contains(&j) {
            intercept_indices.push(j);
        }
    }

    let is_discrete= (0..k).filter(|&jj| {
        if intercept_indices.contains(&jj){ false }
        else {
            let col_j= exog_arr.column(jj);
            col_j.iter().all(|&v| v==0.0|| v==1.0)
        }
    }).collect::<Vec<_>>();

    let z_full= exog_arr.dot(&params_arr);
    let phi_vals= z_full.mapv(|z| pdf64(z));

    let mut sum_ame= vec![0.0_f64; k];
    let mut partial_jl_sums= vec![0.0_f64; k*k];

    // discrete
    for &j in &is_discrete {
        if intercept_indices.contains(&j){ continue;}
        let beta_j= params_arr[j];
        let col_j= exog_arr.column(j);
        let delta_j1= col_j.mapv(|x| if x==0.0 {beta_j}else{0.0});
        let delta_j0= col_j.mapv(|x| if x==1.0 {-beta_j}else{0.0});
        let z_j1= &z_full+ &delta_j1;
        let z_j0= &z_full+ &delta_j0;

        let cdf_j1= z_j1.mapv(|z| cdf64(z));
        let cdf_j0= z_j0.mapv(|z| cdf64(z));
        sum_ame[j]+= cdf_j1.sum()- cdf_j0.sum();

        let pdf_j1= z_j1.mapv(|z| pdf64(z));
        let pdf_j0= z_j0.mapv(|z| pdf64(z));
        let diff_pdf= &pdf_j1- &pdf_j0;
        for l in 0..k {
            if l== j {
                partial_jl_sums[j*k + l]+= pdf_j1.sum();
            } else {
                partial_jl_sums[j*k + l]+= diff_pdf.dot(&exog_arr.column(l));
            }
        }
    }
    // continuous
    for j in 0..k {
        if intercept_indices.contains(&j) || is_discrete.contains(&j){
            continue;
        }
        let beta_j= params_arr[j];
        let sum_phi= phi_vals.sum();
        sum_ame[j]+= beta_j* sum_phi;

        let pprime= &z_full* &phi_vals* -1.0;
        let mut M= exog_arr.to_owned();
        for (i, mut row_i) in M.outer_iter_mut().enumerate() {
            let sc= pprime[i];
            row_i.mapv_inplace(|val| val* sc);
        }
        let col_sums= M.sum_axis(Axis(0));
        for l in 0..k {
            let mut val= beta_j* col_sums[l];
            if l== j {
                val+= sum_phi;
            }
            partial_jl_sums[j*k + l]+= val;
        }
    }

    let ame: Vec<f64>= sum_ame.iter().map(|v| v/(n as f64)).collect();
    let mut grad_ame= Array2::<f64>::zeros((k,k));
    for j in 0..k {
        for l in 0..k {
            grad_ame[(j,l)] = partial_jl_sums[j*k + l]/(n as f64);
        }
    }
    let cov_ame= grad_ame.dot(&cov_arr).dot(&grad_ame.t());
    let var_ame= cov_ame.diag().mapv(|v| v.max(0.0));
    let se_ame= var_ame.mapv(|v| v.sqrt());

    let add_stars= |p:f64|-> &'static str {
        if p<0.01 {"***"}
        else if p<0.05 {"**"}
        else if p<0.1 {"*"}
        else {""}
    };

    let mut dy_dx=vec![];
    let mut se_err=vec![];
    let mut z_vals=vec![];
    let mut p_vals=vec![];
    let mut sig=vec![];
    let mut names=vec![];

    for j in 0..k {
        if intercept_indices.contains(&j){ continue; }
        let val= ame[j];
        let se= se_ame[j];
        let z= if se>0.0 { val/se } else { f64::NAN };
        let p= 2.0*(1.0- cdf64(z.abs()));
        dy_dx.push(val);
        se_err.push(se);
        z_vals.push(z);
        p_vals.push(p);
        sig.push(add_stars(p));
        names.push(exog_names[j].clone());
    }

    let pd= py.import("pandas")?;
    let data= PyDict::new(py);
    data.set_item("dy/dx", dy_dx)?;
    data.set_item("Std. Err", se_err)?;
    data.set_item("z", z_vals)?;
    data.set_item("Pr(>|z|)", p_vals)?;
    data.set_item("Significance", sig)?;

    let kwargs= PyDict::new(py);
    kwargs.set_item("data", data)?;
    kwargs.set_item("index", names)?;

    Ok(pd.call_method("DataFrame", (), Some(kwargs))?)
}

#[pymodule]
fn febolt(_py: Python, m: &PyModule)-> PyResult<()> {
    m.add_function(wrap_pyfunction!(fit_probit, m)?)?;
    m.add_function(wrap_pyfunction!(ame, m)?)?;
    Ok(())
}
