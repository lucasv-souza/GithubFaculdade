#include <stdio.h>
//Lucas Vincius de Souza
//RA: 22504534
int main() {
    int inter, gremio, novo;
    int total = 0, vInter = 0, vGremio = 0, empates = 0;

    do {
        scanf("%d %d", &inter, &gremio);

        if (inter > gremio)
            vInter++;
        else if (gremio > inter)
            vGremio++;
        else
            empates++;

        total++;

        printf("Novo grenal (1-sim 2-nao)\n");
        scanf("%d", &novo);
    } while (novo == 1);

    printf("%d grenais\n", total);
    printf("Inter:%d\n", vInter);
    printf("Gremio:%d\n", vGremio);
    printf("Empates:%d\n", empates);

    if (vInter > vGremio)
        printf("Inter venceu mais\n");
    else if (vGremio > vInter)
        printf("Gremio venceu mais\n");
    else
        printf("Nao houve vencedor\n");

    return 0;
}