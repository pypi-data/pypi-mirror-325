fn main() {
    let res: Result<<Vec<Box<String>>, PyErr> = Python::with_gil(|py|{
        let pl = py.import_bound('polars')?;
        let read_excel = pl.call_method1('read_excel', ('path'))
        let df: Vec<Box<String>> = read_excel..expect("REASON").call1(("E:\gitee\test办公用品库1.xlsx",))?;
        Ok(df)
    });
    match res {
        Ok(df) => {
            println!("{:?}", df);
        }
        Err(err) => {
            println!("{:?}", err.to_string());
        }
    }
;}