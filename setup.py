from distutils.core import setup, Extension
import numpy

pauli_lcu_module = Extension('pauli_lcu_module',
                             sources=['src/c/python_bindings.cpp'],
                             define_macros=[('NPY_NO_DEPRECATED_API', '7')],
                             include_dirs=[numpy.get_include()])

setup(ext_modules=[pauli_lcu_module])
