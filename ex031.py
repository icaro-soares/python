dist = float(input('Qual a distância da viagem (km): '))
# preço = dist * 0.50 if dist <= 200 else dist * 0.45
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print(f'O valor da viagem será R${valor:.2f}')
