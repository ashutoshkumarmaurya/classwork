#include <stdio.h>
#include <stdlib.h>

// implement 1 and 3 option solution.
// implement goto for insertion of all position
// implement a key for exit program.
// ancc B
int main()
{
    int a[10], opt, pos, value, exe;
    int i;
    for (i = 0; i < 10; i++)
    {
        a[i] = 0;
    }
start:
    printf("1. insert on first position\n");
    printf("2. insert on given position\n");
    printf("3. insert on last position\n");
    printf("4. insert to exit\n");
    scanf("%d", &opt);
    switch (opt)
    {
    case 1:
        pos = 0;
        break;
    case 2:
        printf("Enter you position within 0-9\n");
        scanf("%d", &pos);
        break;
    case 3:
        pos = 9;
        break;
    case 4:
        goto end;
        break;

    default:
        printf("You have entered wrong option\n");
        printf("Enter correct option.\n");
        goto start;
        break;
    }
    printf("Enter value for the position \n");
    scanf("%d", &value);
    a[pos] = value;
    for (i = 0; i < 10; i++)
    {
        printf("Current array is: %d\n", a[i]);
    }
    printf("Enter 1 to re insert\n");
    printf("Enter 2 to exit\n");
    scanf("%d", &exe);
    if (exe == 1)
    {
        goto start;
    
    }
    end:
    return 0;
}