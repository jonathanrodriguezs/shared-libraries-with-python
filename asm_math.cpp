#include <iostream>

/** Sum two numbers with ASM */
extern "C" long long sum(long long a, long long b)
{
  long long result;
  __asm__("addl %%ebx, %%eax;"
          : "=a"(result)
          : "a"(a), "b"(b));
  printf("%lld + %lld = %lld\n", a, b, result);
  return result;
}

/** Retrieve the n fibonacci number in the sequence */
extern "C" double fibonacci(int n)
{
  double a = 0, b = 1, c;
  if (n == 0)
    return a;
  for (int i = 2; i <= n; i++)
  {
    c = a + b;
    a = b;
    b = c;
  }
  return b;
}
