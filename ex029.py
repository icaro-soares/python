vel = float(input('Digite a velocidade (km/h): '))
if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print(f'O valor de sua multa é R${multa:.2f}')
else:
    print('Pode prosseguir, tenha um bom dia!')
