### Tests and linter status:   
[![Actions Status](https://github.com/aasineln/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/aasineln/python-project-50/actions)
[![QA SonarQube](https://sonarcloud.io/api/project_badges/measure?project=aasineln_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=aasineln_aasineln_python-project-50)


# Difference Calculator (gendiff)

**Difference Calculator** is a CLI tool that compares two configuration files and displays the differences. It supports JSON and YAML formats, with multiple output styles.

This project was developed as part of the Hexlet.io curriculum, demonstrating:
- Command-line argument parsing using `argparse`
- Recursive comparison of nested data structures
- Multiple output formatters (stylish, plain, JSON)
- Test coverage and static analysis with `ruff`

## Requirements

- Python 3.12 or higher
- `uv` (recommended) 

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/aasineln/python-project-50.git
   cd python-project-50
```
   
2. Install dependencies and the package in development mode:
```bash
    make install
```

## Usage
Basic syntax:
```bash
  gendiff [options] <filepath1> <filepath2>
```

Options:
    `-h, --help` — show help message  
    `-f, --format <format>` — output format: stylish (default), plain, or json

Examples  
```bash
# Compare two JSON files in default stylish format
gendiff file1.json file2.json

# Compare YAML files in plain text format
gendiff --format plain file1.yml file2.yml

# Get JSON output for further processing
gendiff -f json file1.json file2.json
```

## Available Make Commands
```bash
make install        # Install dependencies
make lint           # Run ruff linter
make test           # Run tests
make test-coverage  # Run tests with coverage report
make build          # Build the package
```