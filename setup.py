from setuptools import setup, find_packages, Extension
import numpy

pauli_lcu_module = Extension('pauli_lcu_module',
                             sources=['src/c/python_bindings.cpp'],
                             define_macros=[('NPY_NO_DEPRECATED_API', '7')],
                             include_dirs=[numpy.get_include()])

setup(name="pauli_lcu",
      version="1.0.0",
      description=
      "Decomposition of a matrix into Pauli strings (compiled by MSVC)",
      packages=['pauli_lcu'],
      package_dir={'': 'src'},
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      ext_modules=[pauli_lcu_module])
