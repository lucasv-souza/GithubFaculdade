#include <stdio.h>
#include <math.h>

int main()
{
    int N;

    scanf("%d", &N);

    if (N > 2 && N < 1000){
        for(int i = 1; i <= 10; i++){
            printf("%d x %d = %d\n", i, N, i * N);
        }
    }

    return 0;
}