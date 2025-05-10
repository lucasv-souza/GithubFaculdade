#include <stdio.h>
int main() 
{
    int cod1, cod2, qtd1, qtd2;
    float preco1, preco2, total;

    scanf("%d %d %f", &cod1, &qtd1, &preco1);
    scanf("%d %d %f", &cod2, &qtd2, &preco2);
    total = (qtd1 * preco1) + (qtd2 * preco2);
    printf("VALOR A PAGAR: R$ %.2f\n", total);

    return 0;
}