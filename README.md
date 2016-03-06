[![Build Status](https://travis-ci.org/asottile/setuptools-golang.svg?branch=master)](https://travis-ci.org/asottile/setuptools-golang)
[![Coverage Status](https://img.shields.io/coveralls/asottile/setuptools-golang.svg?branch=master)](https://coveralls.io/r/asottile/setuptools-golang)

setuptools-golang
===================

A setuptools extension for building cpython extensions written in golang.

## Requirements

This requires golang >= 1.5 to be installed on your system.

## Usage

Add `setuptools-golang` to the `setup_requires` in your setup.py and
`build_golang=True`.

```python
setup(
    ...
    build_golang=True,
    setup_requires=['setuptools-golang'],
    ...
)
```

## Writing cpython extensions in golang

TODO
