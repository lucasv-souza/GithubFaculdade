#include <stdio.h>

int main() 
{
    int N;
    float a, b, c, media;

    scanf("%d", &N);

    for(int i = 0; i < N; i++) {
        scanf("%f %f %f", &a, &b, &c); // Lê 3 valores reais
        media = (a * 2 + b * 3 + c * 5) / 10.0; // Média ponderada
        printf("%.1f\n", media); // imprime com 1 casa decimal
    }

    return 0;
}