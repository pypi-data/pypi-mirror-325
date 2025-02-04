from setuptools import setup, find_packages, Extension
from distutils.command.build import build
import os
import shutil
import sys

testy_c_module = Extension(
    'testy_c_module',
    sources=['testy_mnm/core/src/module.c'],
)

class CustomBuild(build):
    def run(self):
        # Run the standard build command
        build.run(self)
        
        # Find the built .pyd/.so file
        extension_path = None
        for root, _, files in os.walk(self.build_lib):
            for file in files:
                if file.startswith('testy_c_module') and (file.endswith('.pyd') or file.endswith('.so')):
                    extension_path = os.path.join(root, file)
                    break
        
        if extension_path:
            # Create core directory if it doesn't exist
            dest_dir = os.path.join('testy_mnm', 'core')
            os.makedirs(dest_dir, exist_ok=True)
            
            # Copy the extension to core directory
            dest_path = os.path.join(dest_dir, os.path.basename(extension_path))
            shutil.copy2(extension_path, dest_path)

setup(
    name='testy_mnm',
    version='0.4',
    cmdclass={'build': CustomBuild},
    packages=find_packages(),
    ext_modules=[testy_c_module],
)
