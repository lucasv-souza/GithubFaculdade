from prova5_1 import DispositivoEletronico, Smartphone, Notebook

if __name__ == "__main__":
    print("--- Início do Sistema de Dispositivos ---")

    print("\n--- Superclasse: DispositivoEletronico ---")
    disp1 = DispositivoEletronico("Samsung", 2500.00)
    disp2 = DispositivoEletronico("LG", 1500.00)

    print(f"Dados Iniciais Dispositivo 1: {disp1.get_marca()}, R$ {disp1.get_preco():.2f}")
    disp1.set_marca("Samsung Brasil")
    disp1.set_preco(2600.00)
    disp1.set_preco(-50)
    print(f"Dados Alterados Dispositivo 1: {disp1.get_marca()}, R$ {disp1.get_preco():.2f}")

    print(f"\nDados Iniciais Dispositivo 2: {disp2.get_marca()}, R$ {disp2.get_preco():.2f}")
    disp2.set_preco(1450.50)
    print(f"Dados Alterados Dispositivo 2: {disp2.get_marca()}, R$ {disp2.get_preco():.2f}")

    print("\n\n--- Subclasse 1: Smartphone ---")
    
    smart1 = Smartphone("Apple", 7000.00, "iOS")
    smart2 = Smartphone("Motorola", 1800.00)

    print(f"\nDados Iniciais Smartphone 1 (3 args): {smart1.get_marca()}, R$ {smart1.get_preco():.2f}, SO: {smart1.get_sistema_op()}")
    smart1.set_sistema_op("Android")
    smart1.set_sistema_op("iOS")
    print(f"Dados Alterados Smartphone 1: SO: {smart1.get_sistema_op()}")

    print(f"\nDados Iniciais Smartphone 2 (2 args): {smart2.get_marca()}, R$ {smart2.get_preco():.2f}, SO: {smart2.get_sistema_op()}")
    smart2.set_sistema_op("iOS")
    print(f"Dados Alterados Smartphone 2: SO: {smart2.get_sistema_op()}")

    print("\n\n--- Subclasse 2: Notebook ---")

    note1 = Notebook("Dell", 4500.00, 16)
    note2 = Notebook("Lenovo", 3200.00)

    print(f"\nDados Iniciais Notebook 1 (3 args): {note1.get_marca()}, R$ {note1.get_preco():.2f}, RAM: {note1.get_ram_gb()}GB")
    note1.set_ram_gb(10)
    note1.set_ram_gb(32)
    print(f"Dados Alterados Notebook 1: RAM: {note1.get_ram_gb()}GB")

    print(f"\nDados Iniciais Notebook 2 (2 args): {note2.get_marca()}, R$ {note2.get_preco():.2f}, RAM: {note2.get_ram_gb()}GB")
    note2.set_ram_gb(12)
    print(f"Dados Alterados Notebook 2: RAM: {note2.get_ram_gb()}GB")

    print("\n\n--- Herança (Métodos Super em Sub) ---")
    print(f"Marca inicial do Smartphone 1: {smart1.get_marca()}")
    smart1.set_marca("Apple Brasil")
    print(f"Marca alterada do Smartphone 1: {smart1.get_marca()}")

    print(f"\nPreço inicial do Notebook 1: R$ {note1.get_preco():.2f}")
    note1.set_preco(4650.00)
    print(f"Preço alterado do Notebook 1: R$ {note1.get_preco():.2f}")

    print("\n\n--- Método Compartilhado (calcular_desconto) ---")
    print(f"Preço do Dispositivo 1 ('{disp1.get_marca()}') antes: R$ {disp1.get_preco():.2f}")
    disp1.calcular_desconto(10)
    print(f"Preço do Dispositivo 1 depois: R$ {disp1.get_preco():.2f}")

    print(f"\nPreço do Smartphone 1 ('{smart1.get_marca()}') antes: R$ {smart1.get_preco():.2f}")
    smart1.calcular_desconto(5)
    print(f"Preço do Smartphone 1 depois: R$ {smart1.get_preco():.2f}")

    print(f"\nPreço do Notebook 1 ('{note1.get_marca()}') antes: R$ {note1.get_preco():.2f}")
    note1.calcular_desconto(20)
    print(f"Preço do Notebook 1 depois: R$ {note1.get_preco():.2f}")