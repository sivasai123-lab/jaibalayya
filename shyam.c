#include<stdio.h>
#include<math.h>
int main()
{
    int fact=1,i,s;
    scanf("%d",&s);
    for(i=1;i<=s;i++)
    {
        fact=fact*i;
    }
    printf("%d",fact);
    return 0;
}
