from setuptools import setup, find_packages, Extension
from distutils.command.build import build
import os

testy_c_module = Extension(
    'testy_c_module',
    sources=['testy_mnm/core/src/module.c'],
)

class CustomBuild(build):
    def finalize_options(self):
        build.finalize_options(self)
        self.build_lib = os.path.join('testy_mnm', 'core')

setup(
    name='testy_mnm',
    version='0.2',
    cmdclass={'build': CustomBuild},
    packages=find_packages(),
    ext_modules=[testy_c_module],
)
