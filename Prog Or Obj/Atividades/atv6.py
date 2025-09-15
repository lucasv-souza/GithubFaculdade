class Aluno:
    def __init__ (self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade

    def get_nome(self):
        return self.nome
    
    def get_mensalidade(self):
        return self.mensalidade
    
    def get_idade(self):
        return self.idade
    
    def set_nome(self, novoNome):
        self.nome = novoNome

    def set_mensalidade(self, novaMensalidade):
        self.mensalidade = novaMensalidade

    def set_idade(self, novaIdade):
        self.idade = novaIdade

if __name__ == '__main__':

    aluno1 = Aluno('Lucas', 1100, 18)
    print("Endereço hexadecimal do Aluno 1:", aluno1)
    print("- Aluno 1:\nNome:", aluno1.get_nome())
    print("Mensalidade:", aluno1.get_mensalidade())
    print("Idade:", aluno1.get_idade())

    aluno1.set_nome("Lucas Vinicius")
    print("Nome Atualizado:", aluno1.get_nome())

    aluno2 = Aluno('Breno', 1300, 24)
    print("Endereço hexadecimal do Aluno 2:", aluno2)
    print("- Aluno 2:\nNome:", aluno2.get_nome())
    print("Mensalidade:", aluno2.get_mensalidade())
    print("Idade:", aluno2.get_idade())

    aluno2.set_nome("Breno Henrique")
    print("Nome Atualizado:", aluno2.get_nome())