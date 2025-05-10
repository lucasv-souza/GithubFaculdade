#include <stdio.h>
int main() 
{
    int numero, horas_trabalhadas;
    float valor_por_hora, salario;

    scanf("%d %d %f", &numero, &horas_trabalhadas, &valor_por_hora);
    salario = horas_trabalhadas * valor_por_hora;

    printf("NUMERO = %d\n", numero);
    printf("SALARIO = R$ %.2f\n", salario);

    return 0;
}