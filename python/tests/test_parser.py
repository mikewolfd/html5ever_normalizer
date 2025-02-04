import pytest
from html5ever_normalizer import parse_html

def test_basic_html_parsing():
    html = "<html><body><h1>Hello World</h1></body></html>"
    result = parse_html(html)
    assert "<html>" in result
    assert "<body>" in result
    assert "<h1>" in result
    assert "Hello World" in result

def test_element_attributes():
    html = '<div class="container" id="main">Content</div>'
    result = parse_html(html)
    assert 'class="container"' in result
    assert 'id="main"' in result
    assert "Content" in result

def test_nested_elements():
    html = "<div><p>First</p><p>Second</p></div>"
    result = parse_html(html)
    assert "<div>" in result
    assert "<p>" in result
    assert "First" in result
    assert "Second" in result
    assert "</p>" in result
    assert "</div>" in result

def test_invalid_html():
    result = parse_html("not valid html <<<")
    assert "not valid html" in result  # html5ever should preserve the text

def test_malformed_html():
    html = "<p>No closing tag"
    result = parse_html(html)
    assert "<p>" in result
    assert "No closing tag" in result
    assert "</p>" in result  # html5ever should fix this

def test_empty_document():
    result = parse_html("")
    assert "<html>" in result
    assert "<head>" in result
    assert "<body>" in result

def test_quirks_mode():
    html = "<p>Test</p>"
    # Test default (limited) mode
    result = parse_html(html)
    assert "<html>" in result
    
    # Test full quirks mode
    result = parse_html(html, quirks_mode="quirks")
    assert "<html>" in result
    
    # Test no quirks mode
    result = parse_html(html, quirks_mode="no-quirks")
    assert "<html>" in result

def test_invalid_quirks_mode():
    # Invalid quirks mode should default to limited quirks
    result = parse_html("<p>Test</p>", quirks_mode="invalid")
    assert "<html>" in result

def test_doctype_preservation():
    # Test that DOCTYPE is preserved (html5ever normalizes to HTML5 DOCTYPE)
    html = '<!DOCTYPE html><html><body>Test</body></html>'
    result = parse_html(html)
    assert '<!DOCTYPE html>' in result
    assert '<html>' in result
    
    # Test that older DOCTYPEs are normalized to HTML5
    html = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
    html += '<html><body>Test</body></html>'
    result = parse_html(html)
    assert '<!DOCTYPE html>' in result  # html5ever normalizes to HTML5 DOCTYPE 