#include <stdio.h>
#include <string.h>

void limpar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    int num_pacientes;
    printf("Quantos pacientes foram atendidos? ");
    scanf("%d", &num_pacientes);
    limpar_buffer();

    if (num_pacientes <= 0) {
        printf("Numero invalido.\n");
        return 1;
    }

    char nome[100], nome_maior_tempo[100];
    int idade, tempo;
    long soma_tempos = 0;
    int maior_tempo = 0;
    int contador_rapidos = 0;
    int contador_idosos = 0;

    for (int i = 0; i < num_pacientes; i++) {
        printf("\n--- Paciente %d ---\n", i + 1);

        printf("Nome: ");
        fgets(nome, sizeof(nome), stdin);
        nome[strcspn(nome, "\n")] = 0;

        printf("Idade: ");
        scanf("%d", &idade);

        printf("Tempo de atendimento (min): ");
        scanf("%d", &tempo);
        limpar_buffer();

        soma_tempos += tempo;
        if (tempo > maior_tempo) {
            maior_tempo = tempo;
            strcpy(nome_maior_tempo, nome);
        }
        if (tempo < 10) {
            contador_rapidos++;
        }
        if (idade >= 60) {
            contador_idosos++;
        }
    }

    printf("\n--- Relatorio Final ---\n");
    printf("Tempo medio de atendimento: %.2f min\n", (double)soma_tempos / num_pacientes);
    printf("Paciente com maior tempo de atendimento: %s (%d min)\n", nome_maior_tempo, maior_tempo);
    printf("Pacientes com menos de 10 min de atendimento: %d\n", contador_rapidos);
    printf("%% de pacientes com 60 anos ou mais: %.2f%%\n", ((double)contador_idosos / num_pacientes) * 100.0);

    return 0;
}