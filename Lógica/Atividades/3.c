#include <stdio.h>
#include <math.h>

int main() {
    double raio = 5; // float e double são a mesma coisa só que com double sendo bem mais preciso
    double pi = 3.14159;
    double area = pi * pow(raio, 2);

    printf("%f", area);

    return 0;
}