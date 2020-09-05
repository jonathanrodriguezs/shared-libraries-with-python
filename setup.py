from setuptools import setup, Extension

# Compile *asm_math.cpp* into a shared library 
setup(ext_modules=[Extension('asm_math', ['asm_math.cpp'],),],)
