# Shared libraries with Python

Use a cpp module with NASM inline using Python3 example.

## Build the shared library
```bash
python compile_libraries.py build
```

## Run the script
```bash
$ python main.py
10 + 100 = 110
Fibonacci 20 is 6765
```

## Run performance test
```bash
$ python performance_test.py
         4 function calls in 1.570 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.158    0.158    1.570    1.570 <string>:1(<module>)
        1    1.403    1.403    1.412    1.412 performance_test.py:5(fib)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.009    0.009    0.009    0.009 {range}


         2 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

## Disclaimer
Tested on Debian 9, linux-x86_64, shared libraries in this OS have the .so extension, in windows this extension is .dll
