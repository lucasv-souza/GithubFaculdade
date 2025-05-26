#include <stdio.h>
//Lucas Vinicius de Souza

int main () 
{
    int hInicio, mInicio, hFim, mFim;
    scanf("%d %d %d %d", &hInicio, &mInicio, &hFim, &mFim);

    int inicio = hInicio * 60 + mInicio;
    int fim = hFim * 60 + mFim;

    if (fim <= inicio) { 
        fim += 24 * 60;
    }

    int duracao = fim - inicio;
    int horas = duracao / 60;
    int minutos = duracao % 60;

    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S) \n", horas, minutos);

    return 0;

}