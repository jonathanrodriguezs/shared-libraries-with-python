#include <iostream>

extern "C" int sum(int a, int b)
{
  int result;
  __asm__("addl %%ebx, %%eax;"
          : "=a"(result)
          : "a"(a), "b"(b));
  printf("%d + %d = %d\n", a, b, result);
  return result;
}

/**
 * Sum two numbers with ASM
 * @param n last fibonacci number
 * @return fibonnaci sequence as array
 */
extern "C" int fibonacci(int n)
{
  int f[n + 2];
  f[0] = 0;
  f[1] = 1;

  for (int i = 2; i <= n; i++)
    f[i] = f[i - 1] + f[i - 2];

  return f[n];
}
