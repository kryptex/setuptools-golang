from setuptools import Extension
from setuptools import setup


setup(
    name='sum_pure_go',
    ext_modules=[Extension('sum_pure_go', ['sum.go', 'sum_support.go'])],
    build_golang=True,
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
