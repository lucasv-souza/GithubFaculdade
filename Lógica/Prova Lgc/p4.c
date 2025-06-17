#include <stdio.h>
#include <string.h>

int main() {
    int qtd_alunos;
    char nomes[30][50];
    float notas[30];
    float soma = 0.0, maior_nota = 0.0;
    int indice_maior = 0;

    // Garantir que o número de alunos esteja entre 1 e 30
    do {
        printf("Informe a quantidade de alunos (1 a 30): ");
        scanf("%d", &qtd_alunos);
    } while (qtd_alunos < 1 || qtd_alunos > 30);

    // Cadastro de alunos
    for (int i = 0; i < qtd_alunos; i++) {
        printf("Digite o nome do aluno %d: ", i + 1);
        getchar(); // Limpa o buffer antes do fgets
        fgets(nomes[i], 50, stdin);
        nomes[i][strcspn(nomes[i], "\n")] = '\0';
        printf("Digite a nota de %s: ", nomes[i]);
        scanf("%f", &notas[i]);

        soma += notas[i];
        if (notas[i] > maior_nota) {
            maior_nota = notas[i];
            indice_maior = i;
        }
    }

    float media = soma / qtd_alunos;

    printf("\nMedia das notas: %.2f\n", media);
    printf("Aluno com a maior nota: %s (%.2f)\n", nomes[indice_maior], maior_nota);

    return 0;
}
// O programa começa validando a entrada da quantidade de alunos com um laço while (na verdade, usei do...while, que também é válido aqui). Depois, usei um for para ler nome e nota de cada aluno. Armazenei os nomes em um vetor de strings (matriz de caracteres) e as notas em um vetor float. Durante a entrada, calculei a soma das notas e identifiquei o aluno com a maior nota. Ao final, exibo a média e o nome do melhor aluno.