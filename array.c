#include<stdio.h>
#include<stdlib.h>

int main()
{
    int i,j,S,R, hold;
    R = 2;
    for(i=0;i<8;i++)
    {
        if(i>3)
        {
            S=i-R;
            R=R+2;
        }
        else
        {
            S=i;
        }
        for(j=0;j<=S;j++)
        {
            printf("*");
        }
        printf("\n");
    }
    scanf("%d", &hold);
}