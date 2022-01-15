from __future__ import annotations

from setuptools import Extension
from setuptools import setup


setup(
    name='sum',
    ext_modules=[
        Extension(
            'sum', ['sum.go'],
            define_macros=[('SUM_A', None), ('SUM_B', '2')],
        ),
    ],
    build_golang={'root': 'github.com/asottile/fake'},
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
