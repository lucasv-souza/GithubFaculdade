#include <stdio.h>
#include <string.h>
#include <ctype.h>

void limpar_buffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    char senha[50];
    int tentativas = 0;
    do {
        printf("Digite a senha: ");
        scanf("%s", senha);
        limpar_buffer();
    } while (strcmp(senha, "estoque2025") != 0 && tentativas++ < 2);

    if (strcmp(senha, "estoque2025") != 0) {
        printf("Acesso negado.\n");
        return 1;
    }
    printf("Acesso liberado!\n\n");

    char nome[100];
    int qtd;
    float preco;
    char continuar = 'S';
    int total_itens = 0;
    double valor_total = 0.0;

    while (toupper(continuar) == 'S') {
        printf("--- Novo Produto ---\n");
        do {
            printf("Nome: ");
            fgets(nome, sizeof(nome), stdin);
            nome[strcspn(nome, "\n")] = 0;
        } while (strlen(nome) == 0);

        do {
            printf("Quantidade: ");
            scanf("%d", &qtd);
        } while (qtd <= 0);

        do {
            printf("Preco: ");
            scanf("%f", &preco);
        } while (preco <= 0);
        
        limpar_buffer();

        total_itens++;
        valor_total += qtd * preco;
        printf("Produto cadastrado.\n");

        do {
            printf("Continuar (S/N)? ");
            continuar = getchar();
            continuar = toupper(continuar);
            limpar_buffer();
        } while (continuar != 'S' && continuar != 'N');
    }

    printf("\n--- Fim ---\n");
    printf("Itens cadastrados: %d\n", total_itens);
    printf("Valor total do estoque: R$ %.2f\n", valor_total);

    return 0;
}