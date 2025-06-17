#include <stdio.h>

int main() {
    int numero_secreto = 42;
    int palpite;

    printf("Tente adivinhar o numero entre 1 e 100.\n");

    do {
        printf("Digite seu palpite: ");
        scanf("%d", &palpite);

        if (palpite > numero_secreto) {
            printf("Palpite alto! Tente um numero menor.\n");
        } else if (palpite < numero_secreto) {
            printf("Palpite baixo! Tente um numero maior.\n");
        }

    } while (palpite != numero_secreto);

    printf("Parabens! Voce acertou o numero %d.\n", numero_secreto);

    return 0;
}
// Utilizei um laço do...while porque era obrigatório no enunciado. Esse tipo de laço garante que pelo menos uma tentativa será feita. O número secreto foi fixado em 42, conforme a instrução. A cada tentativa, o programa informa se o palpite é maior ou menor do que o número secreto. O laço continua até o usuário acertar.