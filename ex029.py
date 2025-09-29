#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro (km/h): '))
if velocidade > 80:
    print('Você foi multado!')
    excedente = velocidade - 80
    multa = excedente * 7.00
    print(f'O valor da multa é de R${multa:.2f}'.replace('.', ','))
else:
    print('Pode passar, siga com segurança! :-D')