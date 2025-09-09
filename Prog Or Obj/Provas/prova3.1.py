class Produto:
    def __init__(self, codigo, nome, preco, quantidade_em_estoque):
        self._codigo = codigo                    
        self._nome = nome                        
        self._preco = preco                       
        self._quantidade_em_estoque = quantidade_em_estoque

    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_quantidade_em_estoque(self):
        return self._quantidade_em_estoque

    def set_codigo(self, novo_codigo):
        self._codigo = novo_codigo

    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self._preco = novo_preco
        else:
            print("Erro: O preço não pode ser negativo.")

    def set_quantidade_em_estoque(self, nova_quantidade):
        if nova_quantidade >= 0:
            self._quantidade_em_estoque = nova_quantidade
        else:
            print("Erro: A quantidade em estoque não pode ser negativa.")

    def registrar_venda(self, quantidade_vendida):
        if quantidade_vendida > 0 and self._quantidade_em_estoque >= quantidade_vendida:
            self._quantidade_em_estoque -= quantidade_vendida
            print(f"Venda de {quantidade_vendida} unidade(s) de '{self.get_nome()}' registrada com sucesso!")
            return True
        else:
            print(f"Falha na venda: estoque insuficiente ou quantidade inválida para '{self.get_nome()}'.")
            return False


if __name__ == "__main__":
    prod1 = Produto("NB-001", "Notebook Ultra Power", 4500.50, 10)
    prod2 = Produto("MS-042", "Mouse Gamer RGB", 250.00, 50)
    prod3 = Produto("KB-117", "Teclado Mecânico", 399.90, 35)

    print("--- ESTADO INICIAL DOS OBJETOS ---")
    print(f"Objeto 1: {prod1.get_nome()}, Estoque: {prod1.get_quantidade_em_estoque()}")
    print(f"Objeto 2: {prod2.get_nome()}, Estoque: {prod2.get_quantidade_em_estoque()}")
    print(f"Objeto 3: {prod3.get_nome()}, Estoque: {prod3.get_quantidade_em_estoque()}")
    print("-" * 35 + "\n")


    print("--- Testando Métodos GET no Objeto 1 (Notebook) ---")
    print(f"Código: {prod1.get_codigo()}")
    print(f"Nome: {prod1.get_nome()}")
    print(f"Preço: R$ {prod1.get_preco():.2f}")
    print(f"Estoque: {prod1.get_quantidade_em_estoque()} unidades")
    print("-" * 35 + "\n")


    print("--- Testando Métodos SET no Objeto 2 (Mouse) ---")
    print(f"Nome antigo: {prod2.get_nome()}")
    prod2.set_nome("Mouse Gamer Sem Fio")  
    print(f"Novo nome: {prod2.get_nome()}")

    print(f"Preço antigo: R$ {prod2.get_preco():.2f}")
    prod2.set_preco(275.50) 
    print(f"Novo preço: R$ {prod2.get_preco():.2f}")
    print("-" * 35 + "\n")


    print("--- Testando Método Funcional 'registrar_venda' no Objeto 3 (Teclado) ---")
    print(f"Estoque inicial de '{prod3.get_nome()}': {prod3.get_quantidade_em_estoque()} unidades.")

    prod3.registrar_venda(5)
    print(f"Estoque atualizado: {prod3.get_quantidade_em_estoque()} unidades.")

    prod3.registrar_venda(50)
    print(f"Estoque permaneceu: {prod3.get_quantidade_em_estoque()} unidades.")
    print("-" * 35 + "\n")