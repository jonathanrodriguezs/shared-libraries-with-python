import cProfile
from setup_libraries import load_asm_math


def performance_test(n):
    result = 0
    for i in range(n):
        result += float(i) * 2
    return result


if __name__ == '__main__':
    asm_math = load_asm_math()

    n = 2500000
    python_result = performance_test(n)
    cpp_result = asm_math.performance_test(n)

    # results printing
    print("performance_test({}) = {:.4f}".format(n, python_result))
    print("asm_math.performance_test({}) = {:.4f}".format(n, cpp_result))

    # profiling
    cProfile.run("performance_test(n)")
    cProfile.run("asm_math.performance_test(n)")
