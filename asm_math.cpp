#include<iostream>

extern "C"

/**
 * Sum two numbers with ASM
 * @return sum
 */
int sum(int a, int b) {
    int result;
    __asm__("addl %%ebx, %%eax;" : "=a" (result) : "a" (a) , "b" (b));
    printf("%d + %d = %d\n", a, b, result);
    return result;
}
