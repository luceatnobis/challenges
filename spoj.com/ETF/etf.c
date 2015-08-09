// http://www.spoj.com/problems/ETF/

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <malloc.h>

uint64_t phi(uint64_t n);

int main(int argc, char *argv[]){
    char *line = NULL;
    uint64_t len = 0;
    uint64_t i, k, testcases;

    getline(&line, &len, stdin);
    testcases = atol(line);
    free(line);
    line = NULL;

    for(i = 0; i < testcases; i++){
        getline(&line, &len, stdin);
        k = atol(line);
        free(line);
        line = NULL;
        printf("%lu\n", phi(k));
    }
    return EXIT_SUCCESS;
}

uint64_t phi(uint64_t n){
    // http://www.geeksforgeeks.org/eulers-totient-function/
    uint64_t p;
    float result = n;   // Initialize result as n

    // Consider all prime factors of n and for every prime
    // factor p, multiply result with (1 - 1/p)
    for (p=2; p*p<=n; ++p)
    {
        // Check if i is a prime factor.
        if (n % p == 0)
        {
            // If yes, then update n and result
            while (n % p == 0)
                n /= p;
            result *= (1 - (1 / (float) p));
        }
    }

    // If n has a prime factor greater than sqrt(n)
    // (There can be at-most one such prime factor)
    if (n > 1)
        result *= (1 - (1 / (float) n));

    return (uint64_t)result;
}
