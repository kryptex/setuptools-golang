from setuptools.dist import Distribution

import setuptools_golang


def test_sets_cmdclass():
    dist = Distribution()
    setuptools_golang.set_build_ext(dist, 'build_golang', True)
    assert dist.cmdclass['build_ext'] == setuptools_golang.BuildExtGolang


def test_sets_cmdclass_value_falsey():
    dist = Distribution()
    setuptools_golang.set_build_ext(dist, 'build_golang', False)
    assert dist.cmdclass.get('build_ext') != setuptools_golang.BuildExtGolang
