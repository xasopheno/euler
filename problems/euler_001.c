#include <stdio.h>

int main(void)
{
    int sum = 0;
    int i;

    for (i = 0; i < 10; i++) {
        if ((i % 3 == 0) || (i % 5 == 0))
            sum += i;
    }

    printf("%d\n", sum);
    return sum;
}
