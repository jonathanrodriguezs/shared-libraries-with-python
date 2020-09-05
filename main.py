from setup_libraries import load_asm_math

if __name__ == "__main__":
    asm_math = load_asm_math()
    asm_math.sum(51230, 12300)  # prints to stdout the result

    fib = asm_math.fibonacci(20)
    print("Fibonacci {} is {:.0f}".format(20, fib))
