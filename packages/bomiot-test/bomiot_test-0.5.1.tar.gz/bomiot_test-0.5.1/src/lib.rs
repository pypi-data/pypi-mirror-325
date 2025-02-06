use pyo3::prelude::*;
use serde_json::Value;
use std::fs;

#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

#[pyfunction]
fn explode<'a>(s: &'a str, sep: &'a str) -> Vec<&'a str> {
    let v = s.split(sep).collect();
    v
}

#[pyfunction]
fn implode(v: Vec<String>, sep: &str) -> String {
    let s = v.join(sep);
    s
}

#[pyfunction]
fn read_json(file_path: &str) -> PyResult<String> {
    // 读取文件内容
    let content = fs::read_to_string(file_path)
        .map_err(|e| pyo3::exceptions::PyIOError::new_err(format!("Failed to read file: {}", e)))?;

    // 解析 JSON
    let json_value: Value = serde_json::from_str(&content)
        .map_err(|e| pyo3::exceptions::PyValueError::new_err(format!("Failed to parse JSON: {}", e)))?;

    // 将 JSON 转换为字符串返回
    Ok(json_value.to_string())
}


// 将函数注册到模块string_utils中
#[pymodule]
fn string_utils(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(explode, m)?)?;
    m.add_function(wrap_pyfunction!(implode, m)?)?;
    m.add_function(wrap_pyfunction!(read_json, m)?)?;
    Ok(())
}