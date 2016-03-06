from setuptools import Extension
from setuptools import find_packages
from setuptools import setup


setup(
    name='project_with_c',
    version='0.1.0',
    packages=find_packages(),
    ext_modules=[
        Extension('project_with_c', ['project_with_c.c']),
        Extension('project_with_c_sum.sum', ['project_with_c_sum/sum.go']),
    ],
    build_golang=True,
    # Would do this, but we're testing *our* implementation and this would
    # install from pypi.  We can rely on setuptools-golang being already
    # installed under test.
    # setup_requires=['setuptools-golang'],
)
