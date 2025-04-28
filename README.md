# astToolkit

A toolkit for manipulating and transforming Python Abstract Syntax Trees (AST).

## Overview

astToolkit provides a rich set of tools for working with Python's AST. Originally part of the [mapFolding](https://github.com/hunterhogan/mapFolding) project, this toolkit has been extracted to provide these capabilities as a standalone package.

## Features

- AST manipulation and transformation utilities
- Code generation tools
- AST traversal and inspection
- Type-safe operations on AST nodes
- Support for Python 3.10+

## Installation

```bash
pip install astToolkit
```

## Usage

```python
from astToolkit import Make, DOT, Be

# Create a basic AST node
node = Make.Name("example")

# Access properties using DOT
name_id = DOT.id(node)

# Check node types
if Be.Name(node):
    print(f"Node is a Name with id: {name_id}")
```

## Requirements

- Python 3.10 or higher

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

This toolkit was developed as part of the [mapFolding](https://github.com/hunterhogan/mapFolding) project and has been separated to enable broader use.

[![CC-BY-NC-4.0](https://github.com/hunterhogan/astToolkit/blob/main/CC-BY-NC-4.0.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
