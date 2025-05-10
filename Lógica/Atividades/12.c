#include <stdio.h>

int main () {

    double N;
    int notas;

    scanf("%lf", &N);

    int valor = (int)N;

    printf("NOTAS: %d\n");

    printf("%d nota(s) R$ 100\n", valor / 100);
    valor %= 100;
    printf("%d nota(s) R$ 50\n", valor / 50);
    valor %= 50;
    printf("%d nota(s) R$ 20\n", valor / 20);
    valor %= 20;
    printf("%d nota(s) R$ 10\n", valor / 10);
    valor %= 10;
    printf("%d nota(s) R$ 5\n", valor / 5);
    valor %= 5;
    printf("%d nota(s) R$ 2\n", valor / 2);
    valor %= 2;
    printf("%d nota(s) R$ 1\n", valor);
    valor %= 1;

    return 0;
}