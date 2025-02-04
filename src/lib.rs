/*!
html5ever_normalizer - Python bindings for html5ever

This crate provides Python bindings for the Rust html5ever library,
offering fast and spec-compliant HTML5 parsing with normalization.
*/

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use html5ever::{parse_document};
use html5ever::serialize::{serialize, SerializeOpts};
use markup5ever_rcdom::{RcDom, SerializableHandle};
use html5ever::tree_builder::QuirksMode;
use html5ever::driver::ParseOpts;
use std::default::Default;
use html5ever::tendril::TendrilSink;

/// Parse an HTML string using html5ever and return the normalized HTML.
///
/// This function takes any HTML string (valid or invalid) and returns a normalized
/// version that follows the HTML5 specification. The input is parsed using html5ever,
/// which automatically handles error recovery and normalization.
///
/// # Arguments
///
/// * `html` - A string slice containing the HTML to parse
/// * `quirks_mode` - Optional string to set the quirks mode: "quirks", "no-quirks", or "limited" (default)
///
/// # Returns
///
/// A String containing the normalized HTML, including DOCTYPE declaration
///
/// # Example
///
/// ```python
/// from html5ever_normalizer import parse_html
/// # Parse with default quirks mode (limited)
/// result = parse_html('<p>Hello World')
/// # Parse with full quirks mode
/// result = parse_html('<p>Hello World', quirks_mode='quirks')
/// # Parse with no quirks mode
/// result = parse_html('<p>Hello World', quirks_mode='no-quirks')
/// ```
#[pyfunction]
#[pyo3(signature = (html, quirks_mode="limited"))]
fn parse_html(html: &str, quirks_mode: &str) -> String {
    let quirks = match quirks_mode {
        "quirks" => QuirksMode::Quirks,
        "no-quirks" => QuirksMode::NoQuirks,
        _ => QuirksMode::LimitedQuirks,
    };

    let opts = ParseOpts {
        tree_builder: html5ever::tree_builder::TreeBuilderOpts {
            quirks_mode: quirks,
            drop_doctype: false,
            ..Default::default()
        },
        ..Default::default()
    };

    // // Parse the HTML input into an RcDom.
    // let dom: RcDom = parse_document(RcDom::default(), opts)
    //     .from_utf8()
    //     .read_from(&mut html.as_bytes())
    //     .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("Parse error: {}", e)))?;

    let dom: RcDom = parse_document(RcDom::default(), opts).one(html);

    let mut output_bytes = Vec::new();
    let serialize_opts = SerializeOpts::default();
    let handle = SerializableHandle::from(dom.document);

    let _ = serialize(&mut output_bytes, &handle, serialize_opts)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("Serialize error: {}", e)));

    String::from_utf8(output_bytes)
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyValueError, _>(format!("UTF-8 error: {}", e))).unwrap()
}

/// Python module for html5ever bindings
#[pymodule]
fn _html5ever_normalizer(py: Python, m: Py<PyModule>) -> PyResult<()> {
    let m = m.bind(py);
    m.add_function(wrap_pyfunction!(parse_html, m)?)?;
    Ok(())
} 
