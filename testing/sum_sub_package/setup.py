from __future__ import annotations

from setuptools import Extension
from setuptools import find_packages
from setuptools import setup


setup(
    name='sum_sub_package',
    ext_modules=[Extension('sum_sub_package.sum', ['sum_sub_package/sum.go'])],
    packages=find_packages(),
    build_golang={'root': 'github.com/asottile/fake', 'strip': False},
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
