[![Build Status](https://travis-ci.org/asottile/setuptools-golang.svg?branch=master)](https://travis-ci.org/asottile/setuptools-golang)
[![Coverage Status](https://img.shields.io/coveralls/asottile/setuptools-golang.svg?branch=master)](https://coveralls.io/r/asottile/setuptools-golang)

setuptools-golang
=================

A setuptools extension for building cpython extensions written in golang.

## Requirements

This requires golang >= 1.5.  It is currently tested against 1.6 and 1.7.

This requires python >= 2.7.  It is currently tested against 2.7, 3.5, 3.6,
and pypy.

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

### ```undefined reference to `some_c_function'```

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

## Building manylinux wheels

`setuptools-golang` also provides a tool for building
[PEP 513](https://www.python.org/dev/peps/pep-0513/) manylinux1 wheels so your
consumers don't need to have a go compiler installed to use your library.

Simply run `setuptools-golang-build-manylinux-wheels` from your source
directory.  The resulting wheels will end up in `./dist`.

```
$ setuptools-golang-build-manylinux-wheels

...

+ ls /dist -al
total 8092
drwxrwxr-x  2 1000 1000    4096 Feb  1 04:16 .
drwxr-xr-x 41 root root    4096 Feb  1 04:15 ..
-rw-r--r--  1 1000 1000 2065095 Feb  1 04:16 setuptools_golang_examples-0.1.1-cp27-cp27mu-manylinux1_x86_64.whl
-rw-r--r--  1 1000 1000 2063299 Feb  1 04:16 setuptools_golang_examples-0.1.1-cp34-cp34m-manylinux1_x86_64.whl
-rw-r--r--  1 1000 1000 2064862 Feb  1 04:16 setuptools_golang_examples-0.1.1-cp35-cp35m-manylinux1_x86_64.whl
-rw-r--r--  1 1000 1000 2064873 Feb  1 04:16 setuptools_golang_examples-0.1.1-cp36-cp36m-manylinux1_x86_64.whl
-rw-rw-r--  1 1000 1000    4273 Feb  1 04:14 setuptools-golang-examples-0.1.1.tar.gz
*******************************************************************************
Your wheels have been built into ./dist
*******************************************************************************
```
