from atv11_1 import Funcionario

if __name__ == '__main__':
  
    f1 = Funcionario('Lucas', 8000.00)
    f2 = Funcionario('Ana', 6000.00)
    print(f"Salário inicial: R$ {f1.get_salario():.2f}")
    f1.set_nome('Lucas Vinícius')
    print(f"Nome atualizado: {f1.nome}")
    f1.aumento_salarial(800.00)
    print(f"Salário atualizado: R$ {f1.get_salario():.2f}")
    print("\n")
    print(f"Salário inicial: R$ {f2.get_salario():.2f}")
    f2.set_nome('Ana Clara')
    print(f"Nome atualizado: {f2.nome}")
    f2.aumento_salarial(500.00)
    print(f"Salário atualizado: R$ {f2.get_salario():.2f}")