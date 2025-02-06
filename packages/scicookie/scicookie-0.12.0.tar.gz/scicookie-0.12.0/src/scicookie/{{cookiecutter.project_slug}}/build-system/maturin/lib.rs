use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn add(x: i64, y: i64) -> i64 {
    x + y
}

#[pyfunction]
fn subtract(x: i64, y: i64) -> i64 {
    x - y
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn {{ cookiecutter.package_slug }}(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    m.add_function(wrap_pyfunction!(subtract, m)?)?;
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;

    Ok(())
}
