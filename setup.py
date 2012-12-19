from setuptools import setup, Extension
setup(
    name='func',
    version='1.0.1',
    description='util functions',
    ext_modules=[Extension('_func', ['funcmodule.c'])],
    py_modules=['func']
)