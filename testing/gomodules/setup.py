from setuptools import Extension
from setuptools import setup


setup(
    name='gomod',
    ext_modules=[Extension('gomodules', ['reversemsg.go'])],
    build_golang={
        'root': 'github.com/asottile/setuptools-golang/testing/gomodules',
    },
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
