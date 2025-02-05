from setuptools import setup
from Cython.Build import cythonize
result_1 = cythonize("src/isoformvisualizer/isoformvisualizer.pyx")
setup(ext_modules=result_1)

