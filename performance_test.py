import cProfile
from setup_libraries import load_asm_math


def fib(n):
    f = [0]*(n+1)
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]


asm_math = load_asm_math()
cProfile.run("fib(250000)")
cProfile.run("asm_math.fibonacci(250000)")
