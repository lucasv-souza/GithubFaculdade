from atv17_1 import Conta_corrente, Conta_poupanca

if __name__ == "__main__":
    cc = Conta_corrente("João", 2000, 500)
    print(f"Conta Corrente - Nome: {cc.nome}, Saldo: R$ {cc.get_saldo()}, Cheque Especial: R$ {cc.cheque_especial}")
    print(f"Saldo Total (incluindo cheque especial): R$ {cc.saldo_total()}")
    
    cp = Conta_poupanca("Maria", 3000, 0.04)
    print(f"\nConta Poupança - Nome: {cp.nome}, Saldo: R$ {cp.get_saldo()}, Porcentagem de Rendimento: {cp.porcentagem_rendimento * 100}%")
    print(f"Saldo Atualizado (após rendimento): R$ {cp.saldo_atualizado()}")