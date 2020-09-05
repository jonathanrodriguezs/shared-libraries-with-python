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

## Disclaimer
Tested on Debian 9, linux-x86_64, shared libraries in this OS have the .so extension, in windows this extension is .dll
