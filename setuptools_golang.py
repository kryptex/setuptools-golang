from __future__ import print_function
from __future__ import unicode_literals

import distutils.sysconfig
import os
import pipes
import subprocess
import sys

from setuptools.command.build_ext import build_ext as _build_ext


PYPY = '__pypy__' in sys.builtin_module_names


def _get_ldflags_pypy():
    if PYPY:  # pragma: no cover (pypy only)
        return '-L{} -lpypy-c'.format(
            os.path.dirname(os.path.realpath(sys.executable)),
        )
    else:
        return None


def _get_ldflags_pkg_config():
    try:
        return subprocess.check_output((
            'pkg-config', '--libs',
            'python-{}.{}'.format(*sys.version_info[:2]),
        )).decode('UTF-8').strip()
    except (subprocess.CalledProcessError, OSError):
        return None


def _get_ldflags_bldlibrary():
    return distutils.sysconfig.get_config_var('BLDLIBRARY')


def _get_ldflags():
    for func in (
            _get_ldflags_pypy,
            _get_ldflags_pkg_config,
            _get_ldflags_bldlibrary,
    ):
        ret = func()
        if ret is not None:
            return ret
    else:
        raise AssertionError('Could not determine ldflags!')


def _print_cmd(env, cmd):
    envparts = [
        '{}={}'.format(k, pipes.quote(v))
        for k, v in sorted(tuple(env.items()))
    ]
    print(
        '$ {}'.format(' '.join(envparts + [pipes.quote(p) for p in cmd])),
        file=sys.stderr,
    )


class build_ext(_build_ext):
    def build_extension(self, ext):
        # If there are no .go files then the parent should handle this
        if not any(source.endswith('.go') for source in ext.sources):
            return _build_ext.build_extension(self, ext)

        for source in ext.sources:
            if not os.path.exists(source):
                raise IOError(
                    'Error building extension `{}`: {} does not exist'.format(
                        ext.name, source,
                    ),
                )

        # Passing non-.go files to `go build` results in a failure
        # Passing only .go files to `go build` causes it to ignore C files
        # So we'll set our cwd to the root of the files and go from there!
        source_dirs = {os.path.dirname(src) for src in ext.sources}
        if len(source_dirs) != 1:
            raise IOError(
                'Error building extension `{}`: '
                'Cannot compile across directories: {}'.format(
                    ext.name, ' '.join(sorted(source_dirs)),
                )
            )
        source_dir, = source_dirs
        source_dir = os.path.abspath(source_dir)

        env = {
            'CGO_CFLAGS': ' '.join(
                '-I{}'.format(p) for p in self.compiler.include_dirs
            ),
            'CGO_LDFLAGS': _get_ldflags(),
        }
        cmd = (
            'go', 'build', '-buildmode=c-shared',
            '-o', os.path.abspath(self.get_ext_fullpath(ext.name)),
        )
        _print_cmd(env, cmd)
        subprocess.check_call(
            cmd, cwd=source_dir, env=dict(os.environ, **env),
        )


def set_build_ext(dist, attr, value):
    if not value:
        return
    dist.cmdclass['build_ext'] = build_ext
