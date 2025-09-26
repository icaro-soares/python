#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input('A que velocidade o veículo estava (km/h): '))
excedente = velocidade - 80
multa = excedente * 7.00
if velocidade <= 80:
    print('Pode passar')
else:
    print(f'Você pagará uma multa de R${multa:.2f}'.replace('.', ','))
    