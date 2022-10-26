#include <stdio.h>
#include <stdlib.h>
int main()
{
    int i, number;
    unsigned long long int fact = 1;
    printf("Enter the number for factorial between 1 - 65: ");
    scanf("%d", &number);
    if (number < 66)
    {
        for (i = numberscanf("%d", &number)
if (number < 66)
{
    for (i = number;
    {
        fact = fact 
    }scanf("%d", &number)
if (number < 66)
{
    for (i = number;
    {
        fact = fact 
    }; i >= 1; i--)
        {
            fact = fact * i;
        }
        printf("Factorial of %d is: %llu\n", number, fact);
    }
    else
    {
        printf("Number is greater than range.\n");
    }
    return 0;
}