from setuptools.command.build_ext import build_ext


class BuildExtGolang(build_ext):
    pass


def set_build_ext(dist, attr, value):
    if not value:
        return
    dist.cmdclass['build_ext'] = BuildExtGolang
