# -*- coding: utf-8 -*-

import sys
from glob import glob
from setuptools import setup, Extension
from distutils.command.build import build


with open('README.md') as f:
    long_description = f.read()

include_dirs = ['src']
libraries = ['speexdsp', 'stdc++']
define_macros = []
extra_compile_args = []

sources = (
    glob('src/noise_suppression.cpp') +
    ['src/speexdsp_ns.i']
)

swig_opts = (
    ['-c++'] +
    ['-I' + h for h in include_dirs]
)


setup(
    name='speexdsp_ns',
    version='0.1.2',
    description='Python bindings of speexdsp noise suppression library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Lucky Wong',
    url='https://github.com/TeaPoly/speexdsp-ns-python',
    packages=['speexdsp_ns'],
    ext_modules=[
        Extension(
            name='speexdsp_ns._speexdsp_ns',
            sources=sources,
            swig_opts=swig_opts,
            include_dirs=include_dirs,
            libraries=libraries,
            define_macros=define_macros,
            extra_compile_args=extra_compile_args
        )
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: C++'
    ],
    license='BSD',
    keywords=['speexdsp_ns', 'acoustic noise suppression'],
    platforms=['Linux'],
    package_dir={
        'speexdsp_ns': 'src'
    }
)
