from setuptools import setup
from Cython.Build import cythonize
result_1 = cythonize("src/imppkg/harmonic_mean.pyx")
setup(ext_modules=result_1)

