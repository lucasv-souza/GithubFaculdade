from provaextra_1 import ContaBancaria, ContaCorrente, ContaPoupanca

if __name__ == "__main__":

    print("--- ContaBancaria ---")
    try:
        conta_abstrata = ContaBancaria("Fantasma", "000", "000-0")
    except TypeError as e:
        print(f"Sucesso: Classe Abstrata não pode ser instanciada.")
        print(f"Erro recebido: {e}\n")


    print("\n--- ContaCorrente ---")
    
    cc1 = ContaCorrente("Ana Silva", "001", "111-1", 1000.0, 500.0)
    cc2 = ContaCorrente("Bruno Costa", "001", "222-2")
    
    print("\n-- Objeto 1 --")
    print(f"Titular: {cc1.get_titular()}, Saldo: R$ {cc1.get_saldo():.2f}")
    cc1.set_titular("Ana S. Souza")
    cc1.set_titular("X")
    print(f"Novo Titular: {cc1.get_titular()}")
    cc1.depositar(200.50)
    cc1.sacar(150.0)
    print(f"Limite Cheque Especial: R$ {cc1.get_limite_cheque_especial():.2f}")
    cc1.set_limite_cheque_especial(-100)
    cc1.calcular_taxa_mensal()
    print(f"Saldo pós-taxa: R$ {cc1.get_saldo():.2f}")
    print(f"Limite total (Saldo + Limite): R$ {cc1.consultar_limite_total():.2f}")

    print("\n-- Objeto 2 --")
    print(f"Titular: {cc2.get_titular()}, Saldo (default): R$ {cc2.get_saldo():.2f}, Limite (default): R$ {cc2.get_limite_cheque_especial():.2f}")
    cc2.depositar(50)


    print("\n\n--- ContaPoupanca ---")

    cp1 = ContaPoupanca("Carla Dias", "002", "333-3", 5000.0, 0.006)
    cp2 = ContaPoupanca("Daniel Emas", "002", "444-4")

    print("\n-- Objeto 1 --")
    print(f"Titular: {cp1.get_titular()}, Saldo: R$ {cp1.get_saldo():.2f}")
    cp1.depositar(1000)
    cp1.sacar(500)
    print(f"Taxa de Rendimento: {cp1.get_taxa_rendimento()*100:.1f}%")
    cp1.set_taxa_rendimento(2.0)
    cp1.set_taxa_rendimento(0.007)
    print(f"Nova Taxa: {cp1.get_taxa_rendimento()*100:.1f}%")
    cp1.calcular_taxa_mensal()
    cp1.aplicar_rendimento()
    print(f"Saldo pós-rendimento: R$ {cp1.get_saldo():.2f}")

    print("\n-- Objeto 2 --")
    print(f"Titular: {cp2.get_titular()}, Saldo (default): R$ {cp2.get_saldo():.2f}, Taxa (default): {cp2.get_taxa_rendimento()*100:.1f}%")
    cp2.depositar(200)
    cp2.aplicar_rendimento()
    print(f"Saldo pós-rendimento: R$ {cp2.get_saldo():.2f}")