#include <stdio.h>
//Lucas Vincius de Souza
//RA: 22504534
int main() 
{
    int valor, maior = 0, posicao = 0;

    for(int i = 1;i <= 100; i++) {
        scanf("%d", &valor);
        if (valor > maior) {
            maior = valor;
            posicao = i;
        }
    }

    printf("%d\n", maior);
    printf("%d\n", posicao);

    return 0;
}