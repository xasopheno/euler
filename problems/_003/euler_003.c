#include <stdio.h>

int main()
{
    long long int i, maxPrimeFactor = 0, n = 600851475143;
    for (i = 2; i < n/2; i ++) {
       while (!(n % i)) {
          n = n / i;
          maxPrimeFactor = n;
       }
    }
    printf("%1lld\n", maxPrimeFactor);
}
