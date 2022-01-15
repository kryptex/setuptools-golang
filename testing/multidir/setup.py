from __future__ import annotations

from setuptools import Extension
from setuptools import setup


setup(
    name='multidir',
    ext_modules=[
        Extension(
            'multidir', ['dir1/sum.go', 'dir2/sum_support.go'],
        ),
    ],
    build_golang={'root': 'github.com/asottile/fake'},
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
