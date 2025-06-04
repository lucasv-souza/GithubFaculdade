#include <stdio.h>

int min(int a, int b) {
    return a < b ? a : b;
}

int main() {
    int N;
    while (scanf("%d", &N) != EOF) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int val = 1 + min(min(i, j), min(N - 1 - i, N - 1 - j));
                printf("%d", val);
            }
            printf("\n");
        }
        printf("\n"); // linha em branco entre os casos
    }
    return 0;
}