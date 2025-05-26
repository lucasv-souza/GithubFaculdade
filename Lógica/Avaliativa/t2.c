#include <stdio.h>
// Lucas Vinicius de Souza

int main() 
{
    char Lucas[100];
    double salario_fixo, total_vendas, salario_total;

    printf("Nome: ");
    scanf("%s", Lucas);
    printf("Salario fixo: ");
    scanf("%lf", &salario_fixo);
    printf("Total de vendas: ");
    scanf("%lf", &total_vendas);

    salario_total = salario_fixo + (total_vendas * 0.15);
    printf("TOTAL R$ %.2lf\n", salario_total);

    return 0;
}