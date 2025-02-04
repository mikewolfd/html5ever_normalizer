"""
html5ever_normalizer - HTML5 Normalizer and Validator

This package provides Python bindings for the Rust html5ever library,
normalizing any HTML input into a complete, valid HTML5 document.
The library automatically adds required structure, fixes malformed markup,
and ensures consistent output regardless of input format.

Example:
    >>> from html5ever_normalizer import parse_html
    >>> # Any input is normalized into a complete HTML document
    >>> html = '<p>Hello World</p>'
    >>> result = parse_html(html)
    >>> print(result)
    <!DOCTYPE html><html><head></head><body><p>Hello World</p></body></html>
    
    >>> # Malformed HTML is automatically fixed
    >>> result = parse_html('<div>Unclosed div')
    >>> print(result)
    <!DOCTYPE html><html><head></head><body><div>Unclosed div</div></body></html>
    
    >>> # Fragment inputs are properly structured
    >>> result = parse_html('Just some text')
    >>> print(result)
    <!DOCTYPE html><html><head></head><body>Just some text</body></html>

The quirks_mode parameter can be one of:
    - 'limited' (default): Limited quirks mode for modern compatibility
    - 'quirks': Full quirks mode for legacy compatibility
    - 'no-quirks': Standard HTML5 parsing

Output Structure:
    The library always produces a complete HTML5 document with:
    1. A normalized DOCTYPE declaration
    2. Required structural elements (html, head, body)
    3. Proper nesting and closing of all tags
    4. Consistent structure regardless of input format
"""

from ._html5ever_normalizer import parse_html

__version__ = "0.1.0"
__all__ = ['parse_html'] 