from prova4_1 import Funcionario, Gerente

if __name__ == "__main__":
    print("--- Início do Sistema da Empresa ---")

    print("\n--- Classe Funcionario ---")
    func1 = Funcionario("Ana Silva", "F001", 3500.00)
    func2 = Funcionario("Bruno Costa", "F002", 4200.00)

    print(f"Dados Iniciais Funcionário1: {func1.get_nome()}, Salário: R$ {func1.get_salario():.2f}")
    func1.set_nome("Ana Carolina Silva")
    func1.set_salario(3800.00)
    func1.set_salario(-500)
    print(f"Dados Alterados Funcionário1: {func1.get_nome()}, Salário: R$ {func1.get_salario():.2f}")

    print(f"\nDados Iniciais Funcionário2: {func2.get_nome()}, Matrícula: {func2.get_matricula()}")
    func2.set_matricula("F003")
    print(f"Dados Alterados Funcionário2: {func2.get_nome()}, Matrícula: {func2.get_matricula()}")

    print("\n\n--- Classe Gerente ---")
    gerente1 = Gerente("Carlos Andrade", "G001", 8000.00, "Tecnologia", 5000.00)
    gerente2 = Gerente("Mariana Lima", "G002", 9500.00, "Marketing", 7000.00)

    print(f"Dados Iniciais Gerente1: {gerente1.get_nome()}, Setor: {gerente1.get_setor()}")
    gerente1.set_setor("Desenvolvimento de Software")
    gerente1.set_bonus_anual(-1000)
    print(f"Dados Alterados Gerente1: Setor: {gerente1.get_setor()}, Bônus: R$ {gerente1.get_bonus_anual():.2f}")

    print(f"\nDados Iniciais Gerente2: {gerente2.get_nome()}, Bônus: R$ {gerente2.get_bonus_anual():.2f}")
    gerente2.set_bonus_anual(8500.00)
    print(f"Dados Alterados Gerente2: Bônus: R$ {gerente2.get_bonus_anual():.2f}")

    print("\n\n--- Herança ---")
    print(f"Métodos da superclasse (Funcionario) em um objeto da subclasse (Gerente).")
    print(f"Nome inicial do Gerente1: {gerente1.get_nome()}")
    gerente1.set_nome("Carlos Souza Andrade")
    print(f"Nome alterado do Gerente1: {gerente1.get_nome()}")

    print(f"Salário inicial do Gerente1: R$ {gerente1.get_salario():.2f}")
    gerente1.set_salario(8500.00)
    print(f"Salário alterado do Gerente1: R$ {gerente1.get_salario():.2f}")

    print("\n\n--- Método compartilhado (calcular_aumento) ---")
    print(f"Salário de '{func1.get_nome()}' antes do aumento: R$ {func1.get_salario():.2f}")
    func1.calcular_aumento(10)
    print(f"Salário de '{func1.get_nome()}' depois do aumento: R$ {func1.get_salario():.2f}")

    print(f"\nSalário de '{gerente1.get_nome()}' antes do aumento: R$ {gerente1.get_salario():.2f}")
    gerente1.calcular_aumento(15)
    print(f"Salário de '{gerente1.get_nome()}' depois do aumento: R$ {gerente1.get_salario():.2f}")