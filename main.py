from setup_libraries import load_asm_math

if __name__ == "__main__":
    asm_math = load_asm_math()
    asm_math.sum(10, 100)

    fib = asm_math.fibonacci(20)
    print("Fibonacci {} is {}".format(20, fib))
