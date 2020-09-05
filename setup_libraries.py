import ctypes
import glob


def load_asm_math():
    # Find the shared library
    libfile = glob.glob('build/*/asm_math*.so')[0]

    # Open the shared library .so
    asm_math = ctypes.CDLL(libfile)

    # Tell Python interpreter the argument and result types
    asm_math.sum.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
    asm_math.sum.restype = ctypes.c_longlong

    asm_math.fibonacci.argtypes = [ctypes.c_int]
    asm_math.fibonacci.restype = ctypes.c_double

    return asm_math
