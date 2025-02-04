#!/bin/bash
set -e

# Build the Rust extension in development mode
maturin develop

# Run the tests
pytest python/tests/ 