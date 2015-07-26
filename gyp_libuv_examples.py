#!/usr/bin/env python

import os
import platform
import sys
import subprocess

try:
  import multiprocessing.synchronize
  gyp_parallel_support = True
except ImportError:
  gyp_parallel_support = False

CC = os.environ.get('CC', 'cc')
script_dir = os.path.dirname(__file__)
example_root = os.path.normpath(script_dir)
full_example_root = os.path.abspath(example_root)
uv_root = os.path.join(full_example_root, 'deps', 'libuv')
output_dir = os.path.join(os.path.abspath(example_root), 'out')

sys.path.insert(0, os.path.join(example_root, 'build', 'gyp', 'pylib'))
try:
    import gyp
except ImportError:
    print('You need to run ./configure to get the build/gyp first. See README')
    sys.exit(42)

def host_arch():
    machine = platform.machine()
    if machine == 'i386': return 'ia32'
    if machine == 'x86_64': return 'x64'
    if machine.startWith('arm'): return 'arm'
    if machine.startWith('mips'): return 'mips'
    return machine

def run_gyp(args):
    rc = gyp.main(args)
    if rc != 0:
        print 'Error running gyp'
        sys.exit(rc)

def compiler_version():
  proc = subprocess.Popen(CC.split() + ['--version'], stdout=subprocess.PIPE)
  is_clang = 'clang' in proc.communicate()[0].split('\n')[0]
  proc = subprocess.Popen(CC.split() + ['-dumpversion'], stdout=subprocess.PIPE)
  version = proc.communicate()[0].split('.')
  version = map(int, version[:2])
  version = tuple(version)
  return (version, is_clang)

if __name__ == '__main__':
    args = sys.argv[1:]

    args.append(os.path.join(full_example_root, 'libuv-examples.gyp'))
    common_fn = os.path.join(os.path.abspath(uv_root), 'common.gypi')
    options_fn = os.path.join(os.path.abspath(uv_root), 'options.gypi')

    if os.path.exists(common_fn):
        args.extend(['-I', common_fn])

    if os.path.exists(options_fn):
        args.extend(['-I', options_fn])

    args.append('--depth=' + example_root)

    if '-f' not in args:
        args.extend('-f make'.split())
    if 'eclipse' not in args and 'ninja' not in args:
        args.extend(['-Goutput_dir=' + output_dir])
        args.extend(['--generator-output=' + output_dir])
    (major, minor), is_clang = compiler_version()
    args.append('-Dgcc_version=%d' % (10 * major + minor))
    args.append('-Dclang=%d' % int(is_clang))

    if not any(a.startswith('-Dhost_arch=') for a in args):
        args.append('-Dhost_arch=%s' % host_arch())

    if not any(a.startswith('-Dtarget_arch=') for a in args):
        args.append('-Dtarget_arch=%s' % host_arch())

    if not any(a.startswith('-Duv_library=') for a in args):
        args.append('-Duv_library=static_library')

    if not any(a.startswith('-Dcomponent=') for a in args):
        args.append('-Dcomponent=static_library')

    gyp_args = list(args)
    print gyp_args
    run_gyp(gyp_args)
