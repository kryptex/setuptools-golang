[![Build Status](https://travis-ci.org/asottile/setuptools-golang.svg?branch=master)](https://travis-ci.org/asottile/setuptools-golang)
[![Coverage Status](https://img.shields.io/coveralls/asottile/setuptools-golang.svg?branch=master)](https://coveralls.io/r/asottile/setuptools-golang)

setuptools-golang
=================

A setuptools extension for building cpython extensions written in golang.

## Requirements

This requires golang >= 1.5.  It is currently tested against 1.5 and 1.6.

This requires python >= 2.7.  It is currently tested against 2.7, 3.4, 3.5,
and pypy.

It is incompatible with pypy3 (for now) due to a lack of c-api.

## Usage

Add `setuptools-golang` to the `setup_requires` in your setup.py and
`build_golang={'root': ...}`.  `root` refers to the root go import path of
your project.

An extension must be a single file in the `main` go package (though the entire
`main` package will be built into the extension).  That package may import
other code.
You may have multiple extensions in your `setup.py`.

```python
setup(
    ...
    build_golang={'root': 'github.com/user/project'},
    ext_modules=[Extension('example', ['example.go'])],
    setup_requires=['setuptools-golang'],
    ...
)
```

## Writing cpython extensions in golang

TODO
