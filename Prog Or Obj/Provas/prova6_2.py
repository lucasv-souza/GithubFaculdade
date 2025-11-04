from prova6_1 import Veiculo, Carro, Moto

if __name__ == "__main__":
    print("--- Início do Sistema da Concessionária ---")

    print("\n--- Superclasse: Veiculo ---")
    veiculo_teste = Veiculo("Veículo Genérico", 10000.00)
    
    print(f"Dados Iniciais: {veiculo_teste.get_marca()}, R$ {veiculo_teste.get_preco_base():.2f}")
    veiculo_teste.set_marca("Marca Genérica Alterada")
    veiculo_teste.set_preco_base(11000.00)
    veiculo_teste.set_preco_base(-500)
    print(f"Dados Alterados: {veiculo_teste.get_marca()}, R$ {veiculo_teste.get_preco_base():.2f}")
    
    veiculo_teste.aplicar_desconto(10)
    preco_final_veiculo = veiculo_teste.calcular_preco_com_imposto(7)
    print(f"Preço final com imposto: R$ {preco_final_veiculo:.2f}")


    print("\n\n--- Subclasse 1: Carro ---")
    carro1 = Carro("Honda", 80000.00, 4)
    carro2 = Carro("VW", 75000.00)

    print(f"\nDados Carro 1 (3 args): {carro1.get_marca()}, R$ {carro1.get_preco_base():.2f}, Portas: {carro1.get_numero_portas()}")
    carro1.set_numero_portas(3)
    carro1.set_preco_base(81000.00)
    print(f"Dados Alterados Carro 1: R$ {carro1.get_preco_base():.2f}, Portas: {carro1.get_numero_portas()}")

    print(f"\nDados Carro 2 (2 args): {carro2.get_marca()}, R$ {carro2.get_preco_base():.2f}, Portas: {carro2.get_numero_portas()}")
    carro2.set_numero_portas(2)
    print(f"Dados Alterados Carro 2: Portas: {carro2.get_numero_portas()}")

    carro1.aplicar_desconto(5)
    preco_final_carro = carro1.calcular_preco_com_imposto(15)
    print(f"Preço final Carro 1 com imposto: R$ {preco_final_carro:.2f}")


    print("\n\n--- Subclasse 2: Moto ---")
    moto1 = Moto("Yamaha", 45000.00, 750)
    moto2 = Moto("Suzuki", 38000.00)

    print(f"\nDados Moto 1 (3 args): {moto1.get_marca()}, R$ {moto1.get_preco_base():.2f}, CC: {moto1.get_cilindradas()}")
    moto1.set_cilindradas(20)
    moto1.set_marca("Yamaha Racing")
    print(f"Dados Alterados Moto 1: {moto1.get_marca()}, CC: {moto1.get_cilindradas()}")
    
    print(f"\nDados Moto 2 (2 args): {moto2.get_marca()}, R$ {moto2.get_preco_base():.2f}, CC: {moto2.get_cilindradas()}")
    moto2.set_cilindradas(600)
    print(f"Dados Alterados Moto 2: CC: {moto2.get_cilindradas()}")
    
    moto2.aplicar_desconto(8)
    preco_final_moto = moto2.calcular_preco_com_imposto(5)
    print(f"Preço final Moto 2 com imposto: R$ {preco_final_moto:.2f}")