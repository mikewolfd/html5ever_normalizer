# html5ever_normalizer

A Python binding for the Rust html5ever library that normalizes and validates HTML into a complete, well-structured document.

> This package was developed using [Cursor](https://cursor.sh/) and Claude 3.5 Sonnet.

## Features

- Normalizes any HTML input into a complete, valid HTML5 document
- Automatically adds required structure (html, head, body tags)
- Fixes malformed markup and unclosed tags
- Preserves and normalizes DOCTYPE declarations
- Fast HTML5 parsing using Rust's html5ever
- Support for different quirks modes (limited by default, full, or no-quirks)

## Installation

### From PyPI (Recommended)
```bash
pip install html5ever-normalizer
```

### From GitHub Releases (Pre-built wheels)
You can download pre-built wheels for your platform from the [GitHub Releases page](https://github.com/yourusername/html5ever_normalizer/releases). These wheels are available for:
- Linux (x86_64, aarch64)
- macOS (x86_64 and arm64, compatible with macOS 10.14+)

Python versions 3.10, 3.11, and 3.12 are supported.

### From GitHub Source
```bash
pip install git+https://github.com/yourusername/html5ever_normalizer.git
```

#### System Requirements for Source Installation
When installing from source, you'll need:
- Rust toolchain (install from https://rustup.rs)
- Python 3.8 or later
- A C compiler:
  - Linux: GCC (usually pre-installed)
  - macOS: Xcode Command Line Tools
  - Windows: Microsoft Visual Studio Build Tools

### For Development
```bash
# Clone the repository
git clone https://github.com/yourusername/html5ever_normalizer.git
cd html5ever_normalizer

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Install the package in editable mode
maturin develop
```

## Usage

```python
from html5ever_normalizer import parse_html

# Any input is normalized into a complete HTML document
html = '<p>Hello World</p>'
result = parse_html(html)
print(result)
# Output:
# <!DOCTYPE html>
# <html><head></head><body><p>Hello World</p></body></html>

# Malformed HTML is automatically fixed
html = '<div>Unclosed div'
result = parse_html(html)
print(result)
# Output:
# <!DOCTYPE html>
# <html><head></head><body><div>Unclosed div</div></body></html>

# Fragment inputs are properly structured
html = 'Just some text'
result = parse_html(html)
print(result)
# Output:
# <!DOCTYPE html>
# <html><head></head><body>Just some text</body></html>

# DOCTYPE is preserved but normalized
html = '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">'
result = parse_html(html)
print(result)
# Output:
# <!DOCTYPE html>
# <html><head></head><body></body></html>

# Quirks mode can be specified
result = parse_html(html, quirks_mode='quirks')  # 'limited' (default), 'quirks', or 'no-quirks'
```

### HTML Normalization

The library always produces a complete, valid HTML5 document. This means:

1. A normalized DOCTYPE declaration (`<!DOCTYPE html>`)
2. Required structural elements:
   - `<html>` root element
   - `<head>` section (even if empty)
   - `<body>` section
3. Proper nesting and closing of all tags
4. Handling of HTML fragments by placing them in the appropriate context
5. Consistent output structure regardless of input format

### Quirks Mode

The `parse_html` function accepts a `quirks_mode` parameter that can be one of:
- `'limited'` (default): Limited quirks mode for modern compatibility
- `'quirks'`: Full quirks mode for legacy compatibility
- `'no-quirks'`: Standard HTML5 parsing

## Requirements

- Python 3.8 or later
- Rust toolchain (for building from source)

## License

MIT License. See [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 