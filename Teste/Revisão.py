# Revisão dos Conceitos Fundamentais de Python
'''
### **1. Estruturas de Repetição (Laços `for` e `while`)**

#### **Para que serve?**

Imagine que você precisa executar a mesma tarefa várias vezes, como dar "bom dia" para 100 pessoas. Seria muito ineficiente escrever `print("Bom dia")` 100 vezes. As estruturas de repetição, ou laços (*loops*), servem exatamente para isso: **automatizar tarefas repetitivas**. Elas permitem que você execute um mesmo bloco de código quantas vezes for necessário, seja um número fixo de vezes ou até que uma determinada condição seja satisfeita.

#### **Como funciona?**

Existem dois tipos principais de laços em Python:

1.  **Laço `for` (Laço Contado):** É usado quando você **sabe quantas vezes** quer repetir a tarefa. Ele é ideal para percorrer itens de uma lista, ou para repetir algo um número exato de vezes usando a função `range()`.

      * **Estrutura:** `for item in sequencia:`

2.  **Laço `while` (Laço Condicional):** É usado quando você **não sabe quantas vezes** a tarefa precisa ser repetida. O laço continua executando *enquanto* uma condição for verdadeira.

      * **Estrutura:** `while condicao_verdadeira:`

#### **Código de Exemplo Comentado:**

Neste exemplo, vamos usar um laço `for` para somar os números de uma lista e um laço `while` para um jogo simples de adivinhação.
'''

# --- Exemplo com Laço FOR ---
def somar_notas():
    # Temos uma lista de notas e queremos somar todas elas.
    notas = [8.5, 9.0, 7.5, 10.0, 6.5]
    soma = 0.0 # Variável que vai acumular a soma, começa em zero.

    # O laço 'for' vai passar por cada item da lista 'notas'.
    # A cada repetição, a variável 'nota_atual' receberá o valor de um item.
    print("--- Usando FOR para somar notas ---")
    for nota_atual in notas:
        print(f"Somando a nota: {nota_atual}")
        soma = soma + nota_atual # Adiciona a nota atual à soma total.

    # Após o laço terminar, a variável 'soma' terá o valor total.
    print(f"A soma de todas as notas é: {soma:.2f}")
    print("-" * 20)


# --- Exemplo com Laço WHILE ---
def jogo_adivinhacao():
    numero_secreto = 42 # O número que o usuário deve adivinhar.
    palpite = 0 # Variável para guardar o palpite do usuário, começa com um valor diferente.

    print("--- Usando WHILE para um jogo ---")
    print("Adivinhe o número secreto entre 1 e 100!")

    # O laço 'while' continuará executando ENQUANTO o palpite for diferente do número secreto.
    while palpite != numero_secreto:
        # Pede ao usuário para digitar um número a cada repetição.
        palpite = int(input("Qual o seu palpite? "))

        # Verifica se o palpite está correto. Se não estiver, o laço repetirá.
        if palpite == numero_secreto:
            print("Parabéns! Você acertou o número secreto!")
        else:
            print("Errado! Tente novamente.")

    # O código só chegará aqui quando a condição do 'while' se tornar falsa.
    print("Fim de jogo!")

# --- Programa Principal ---
if __name__ == "__main__":
    somar_notas()
    jogo_adivinhacao()

### **2. Função**

#### **Para que serve?**
'''
Uma função é um **bloco de código nomeado e organizado que executa uma tarefa específica**. Pense nela como uma "receita" ou uma "ferramenta" que você cria para usar sempre que precisar.

As principais vantagens de usar funções são:

  * **Reutilização:** Você escreve o código uma vez e pode "chamar" (executar) a função de vários lugares diferentes do seu programa.
  * **Organização:** Elas dividem um programa grande em partes menores e mais fáceis de entender. Em vez de um único arquivo com 1000 linhas, você pode ter várias funções, cada uma com sua responsabilidade.
  * **Manutenção:** Se você precisar corrigir um erro ou melhorar uma lógica, você só precisa alterar em um lugar: dentro da definição da função.

#### **Como funciona?**

Uma função é definida com a palavra-chave `def`. Ela pode receber dados de entrada (chamados **parâmetros** ou **argumentos**) e pode fornecer um resultado de saída (usando a palavra-chave `return`).

  * `def nome_da_funcao(parametro1, parametro2):` \# A "assinatura" da função
  * `# Código que executa a tarefa` \# O "corpo" da função
  * `return resultado` \# O "resultado" que a função devolve

#### **Código de Exemplo Comentado:**

Neste exemplo, criamos uma função para calcular a área de um retângulo. O programa principal vai pedir os dados, usar a função para fazer o cálculo e exibir o resultado.
'''

# --- DEFINIÇÃO DA FUNÇÃO ---

# Definimos uma função chamada 'calcular_area_retangulo'.
# Ela precisa de dois "ingredientes" (parâmetros): a largura e a altura.
def calcular_area_retangulo(largura, altura):
    # O corpo da função executa a tarefa: calcular a área.
    print(f"\n... Executando a função com largura={largura} e altura={altura} ...")
    area = largura * altura

    # A palavra-chave 'return' envia o resultado do cálculo de volta
    # para onde a função foi chamada.
    return area
    # Fim da função.


# --- PROGRAMA PRINCIPAL ---
# É aqui que o programa começa a ser executado.
if __name__ == "__main__":
    print("--- Calculadora de Área de Retângulo ---")

    # Pedimos os dados ao usuário.
    largura_digitada = float(input("Digite a largura do retângulo: "))
    altura_digitada = float(input("Digite a altura do retângulo: "))

    # Agora, "chamamos" a nossa ferramenta (a função).
    # Passamos os valores digitados como argumentos.
    # A variável 'resultado_area' vai receber o valor que a função RETORNOU.
    resultado_area = calcular_area_retangulo(largura_digitada, altura_digitada)

    # Exibimos o resultado que recebemos da função.
    print(f"A área do retângulo é: {resultado_area}")

    # Podemos REUTILIZAR a função com outros valores!
    print("\n--- Testando a função com outros valores ---")
    area_fixa = calcular_area_retangulo(10, 5) # Chamando com valores fixos
    print(f"A área de um retângulo 10x5 é: {area_fixa}")


### **3. Programação Orientada a Objetos (POO)**

#### **Para que serve?**
'''
A POO é uma forma de pensar e estruturar programas. A ideia principal é **modelar o mundo real dentro do código**. Em vez de pensar em variáveis e funções separadas, você cria **"Objetos"**.

Um objeto é uma entidade que agrupa duas coisas:

1.  **Dados (Atributos):** As características ou informações do objeto. (Ex: a *cor*, o *modelo* e a *velocidade* de um carro).
2.  **Comportamentos (Métodos):** As ações que o objeto pode realizar. (Ex: um carro pode *acelerar*, *frear* e *ligar\_farol*).

Isso torna o código mais intuitivo, organizado e escalável, especialmente para sistemas complexos.

#### **Como funciona?**

  * **Classe:** É o "molde" ou a "planta baixa" para criar objetos. A classe define quais atributos e métodos um objeto daquele tipo terá. (Ex: A classe `Carro`).
  * **Objeto (ou Instância):** É a "construção" feita a partir do molde. É uma entidade real e única criada a partir de uma classe. (Ex: `meu_fusca`, `carro_da_vizinha` são objetos da classe `Carro`).
  * **`__init__` (Construtor):** É um método especial dentro da classe que é executado quando um novo objeto é criado. Ele serve para definir os valores iniciais dos atributos.
  * `self`: É uma palavra-chave especial que, dentro de um método, se refere ao próprio objeto.

#### **Código de Exemplo Comentado:**

Vamos criar uma classe `Cachorro` para modelar cachorros. Cada cachorro (objeto) terá um nome e uma raça (atributos) e poderá latir (método).
'''
# --- DEFINIÇÃO DA CLASSE (O MOLDE) ---

class Cachorro:
    # O método construtor. É chamado quando um novo objeto Cachorro é criado.
    # 'self' se refere ao objeto que está sendo criado.
    # 'nome_inicial' e 'raca_inicial' são os dados que precisamos para criar um cachorro.
    def __init__(self, nome_inicial, raca_inicial):
        print(f"Criando um novo cachorro chamado {nome_inicial}...")
        # ATRIBUTOS: guardamos as informações dentro do objeto usando 'self'.
        self.nome = nome_inicial
        self.raca = raca_inicial
        self.esta_dormindo = False # Todo cachorro começa acordado.

    # MÉTODO: uma ação que o objeto pode fazer.
    def latir(self):
        # Acessamos o atributo 'nome' do próprio objeto com 'self.nome'.
        if self.esta_dormindo:
            print(f"{self.nome} não pode latir, está dormindo... Zzz...")
        else:
            print(f"{self.nome} diz: Au au!")

    def dormir(self):
        self.esta_dormindo = True
        print(f"{self.nome} foi dormir.")


# --- PROGRAMA PRINCIPAL (USANDO OS OBJETOS) ---
if __name__ == "__main__":
    print("--- Bem-vindo ao Canil Virtual ---")

    # Criando nosso primeiro OBJETO (instância) a partir da classe Cachorro.
    # A chamada 'Cachorro(...)' executa o método __init__.
    cachorro1 = Cachorro("Rex", "Pastor Alemão")

    # Criando um segundo OBJETO. Ele é independente do primeiro.
    cachorro2 = Cachorro("Bolinha", "Poodle")

    print("\n--- Interagindo com os cachorros ---")

    # Chamando o método 'latir' do primeiro objeto.
    cachorro1.latir()

    # Chamando o método 'latir' do segundo objeto.
    cachorro2.latir()

    # Alterando o estado do cachorro1.
    cachorro1.dormir()

    # Tentando fazer o cachorro1 latir de novo.
    cachorro1.latir()