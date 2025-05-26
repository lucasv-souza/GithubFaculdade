#include <stdio.h>

int main() 
{
    double A, B, MEDIA;
    double peso_A = 3.5, peso_B = 7.5;

    scanf("%lf %lf", &A, &B);
    MEDIA = ((A * peso_A)+ (B * peso_B)) / (peso_A + peso_B);
    printf("MEDIA = %.5lf\n", MEDIA);

    return 0;
}