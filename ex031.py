#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = int(input('Qual a distância da viagem [km]? '))
print(f'Sua viagem é de {dist}km de distância')
if dist <= 200:
    preço = dist * 0.50
else:
    preço = dist * 0.45
print(f'O preço a pagar será de R${preço:.2f}'.replace('.', ','))
