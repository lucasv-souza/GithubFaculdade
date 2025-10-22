from atv12_1 import Veiculo, Carro, Moto

carro1 = Veiculo(50000, 15000)
print(f"Valor do veículo: R$ {carro1.get_valor():.2f}, Quilometragem: {carro1.get_km()} km")
carro1.set_valor(48000)
carro1.set_km(12000)
print(f"Novo valor do veículo: R$ {carro1.get_valor():.2f}, Quilometragem: {carro1.get_km()} km")

print("\n")

carro1 = Carro(60000, 10000, 4)
carro2 = Carro(30000, 15000)
print(f"Valor Carro 1 : R$ {carro1.get_valor():.2f}, Quilometragem: {carro1.get_km()} km, Quantidade de Portas: {carro1.get_qtd_portas()}")
print(f"Valor Carro 2 : R$ {carro2.get_valor():.2f}, Quilometragem: {carro2.get_km()} km, Quantidade de Portas: {carro2.get_qtd_portas()}")

print("\n")

moto1 = Moto(20000, 8000, 150)
moto2 = Moto(15000, 12000)
print(f"Valor Moto 1 : R$ {moto1.get_valor():.2f}, Quilometragem: {moto1.get_km()} km, Cilindradas: {moto1.get_cilindradas()}")
print(f"Valor Moto 2 : R$ {moto2.get_valor():.2f}, Quilometragem: {moto2.get_km()}, km, Cilindradas: {moto2.get_cilindradas()}")
moto1.atualiza_valor(3500)
print(f"Novo valor Moto 1 : R$ {moto1.get_valor():.2f}, Quilometragem: {moto1.get_km()} km, Cilindradas: {moto1.get_cilindradas()}")