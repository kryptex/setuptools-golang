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

Here's some [examples](https://github.com/asottile/setuptools-golang-examples)

## Common issues

### `undefined reference to \`some_c_function'`

`Extension` by default will bring along the go files listed, but won't bring
along the related C files.  Add the following to `MANIFEST.in`:

```
global-include *.c
global-include *.go
```

### `fatal: could not read Username for 'https://github.com':`

You're probably trying to import from an external source which does not exist.
Double check that your import is correct.


### `package github.com/a/b/c: /tmp/.../github.com/a/b exists but /tmp/.../github.com/a/b/.git does not - stale checkout?`

You've probably mistyped an import.  Double check that your import is correct.
