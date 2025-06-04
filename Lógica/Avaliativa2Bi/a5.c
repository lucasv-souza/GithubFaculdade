#include <stdio.h>
//Lucas Vincius de Souza
//RA: 22504534
int main() {
    int par[5], impar[5];
    int num, i, p = 0, im = 0;

    for (i = 0; i < 15; i++) {
        scanf("%d", &num);
        if (num % 2 == 0) {
            par[p] = num;
            p++;
            if (p == 5) {
                for (int j = 0; j < 5; j++) {
                    printf("par[%d] = %d\n", j, par[j]);
                }
                p = 0;
            }
        } else {
            impar[im] = num;
            im++;
            if (im == 5) {
                for (int j = 0; j < 5; j++) {
                    printf("impar[%d] = %d\n", j, impar[j]);
                }
                im = 0;
            }
        }
    }

    for (int j = 0; j < im; j++) {
        printf("impar[%d] = %d\n", j, impar[j]);
    }
    for (int j = 0; j < p; j++) {
        printf("par[%d] = %d\n", j, par[j]);
    }

    return 0;
}