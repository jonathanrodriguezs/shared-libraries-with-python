import ctypes
import glob
import sys

def load_asm_math():
    # Find the shared library
    libfile = glob.glob('build/*/asm_math*.so')[0]

    # Open the shared library .so
    asm_math = ctypes.CDLL(libfile)

    # Tell Python interpreter the argument and result types of function sum
    asm_math.sum.restype = ctypes.c_longlong
    asm_math.sum.argtypes = [ctypes.c_int, ctypes.c_int]

    return asm_math

if __name__ == "__main__":
    asm_math = load_asm_math()
    a, b = int(sys.argv[1]), int(sys.argv[2])
    asm_math.sum(a, b)
