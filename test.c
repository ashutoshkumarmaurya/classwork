#include <stdio.h>
#include <stdlib.h>

void main()
{
    int a, stop;
    printf("enter the value of a");
    scanf("%d", &a);
    if (a % 100 == 0)
    {
        if (a % 400 == 0)
        {
            printf("a is leap year");
        }

        else
        {
            printf("a is not leap year");
        }
    }
    else if (a % 4 == 0)
    {
        printf("a is leap year");
    }
    else
    {
        printf("a is not leap year");
    }
    scanf("%d", &stop);
}