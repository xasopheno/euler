#include <stdio.h>

int main()
{
    unsigned int i, temp = 0, n = 600;
    for (i = 0; i < n/2; i ++) {
       while (!(n % i)) {
          n = n / i;
          printf("%u\n", n);
       }
    }


}
