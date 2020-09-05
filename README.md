# Shared libraries with Python

Use a cpp module with NASM inline using Python3 example.

## Build the shared library
```bash
python compile_libraries.py build
```

## Run the script
```bash
$ python main.py
51230 + 12300 = 63530
Fibonacci 20 is 6765
```

## Run performance test
```bash
$ python performance_test.py
performance_test(2500000) = 6249997500000.0000 # python
asm_math.performance_test(2500000) = 6249997500000.0000 # cpp shared object
         4 function calls in 0.869 seconds

   Ordered by: standard name # python function execution timing

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.869    0.869 <string>:1(<module>)
        1    0.821    0.821    0.869    0.869 performance_test.py:5(performance_test)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.049    0.049    0.049    0.049 {range}


         2 function calls in 0.005 seconds

   Ordered by: standard name # cpp shared object function execution timing

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.005    0.005    0.005    0.005 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Disclaimer
Tested on Debian 9, linux-x86_64, shared libraries in this OS have the .so extension, in windows this extension is .dll
