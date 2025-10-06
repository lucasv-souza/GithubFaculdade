from atv11_1 import Funcionario, Gerente

if __name__ == '__main__':
  
    f1 = Funcionario("João", 2000)
    g1 = Gerente("Maria", 5000, 10)
    print(f"Funcionário: {f1.get_nome()}, Salário: R$ {f1.get_salario():.2f}")
    print(f"Gerente: {g1.get_nome()}, Salário: R$ {g1.get_salario():.2f}, Quantidade de Gerências: {g1.get_qtd_gerencia()}")
    f1.bonificacao()
    g1.bonificacao()
    print("Após bonificação:")
    
    print(f"Funcionário: {f1.get_nome()}, Salário: R$ {f1.get_salario():.2f}")
    print(f"Gerente: {g1.get_nome()}, Salário: R$ {g1.get_salario():.2f}, Quantidade de Gerências: {g1.get_qtd_gerencia()}")

    f1.set_salario(500)
    g1.set_salario(1000)
    print("Após aumento salarial:")
    print(f"Funcionário: {f1.get_nome()}, Salário: R$ {f1.get_salario():.2f}")
    print(f"Gerente: {g1.get_nome()}, Salário: R$ {g1.get_salario():.2f}, Quantidade de Gerências: {g1.get_qtd_gerencia()}")

    g1.set_qtd_gerencia(15)
    print("Após alteração na quantidade de gerências do gerente:")
    print(f"Gerente: {g1.get_nome()}, Salário: R$ {g1.get_salario():.2f}, Quantidade de Gerências: {g1.get_qtd_gerencia()}")

    f1.set_nome("João Silva")
    g1.set_nome("Maria Souza")
    print("Após alteração nos nomes:")
    print(f"Funcionário: {f1.get_nome()}, Salário: R$ {f1.get_salario():.2f}")
    print(f"Gerente: {g1.get_nome()}, Salário: R$ {g1.get_salario():.2f}, Quantidade de Gerências: {g1.get_qtd_gerencia()}")
