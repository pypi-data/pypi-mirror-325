import os
from setuptools.command.build_ext import build_ext as _build_ext
import numpy as np
from setuptools import setup, find_packages, Extension


this_dir = '.'
core_dir = os.path.join(this_dir, "NChess/core")
build_path = os.path.join(core_dir, "build")

class build_ext(_build_ext):
    def build_extension(self, ext):
        self.compiler.output_dir = core_dir
        _build_ext.build_extension(self, ext)

def find_c_files(directory):
    c_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.c')]
    return c_files

nchess_module = Extension(
    'nchess',
    sources=[
        *find_c_files(os.path.join(core_dir, 'src')),
        *find_c_files(os.path.join(core_dir, 'src/nchess')),
    ],
    include_dirs=[
        "NChess/core/src",
        "NChess/core/src/nchess",
        np.get_include(),
    ],
)

setup(
    name='NChess',
    version='1.0.22',
    ext_modules=[
            nchess_module
        ],
    include_package_data=True,
    install_requires=[
        'numpy>=1.18.0', "wheel", "setuptools>=42"
    ],
    author='MNMoslem',
    author_email='normoslem256@gmail.com',
    description='chess library written in c',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MNourMoslem/NChess',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    license=open('LICENSE').read(),
)
