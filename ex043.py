peso = float(input('Peso (kg): '))
alt = float(input('Altura (m): '))
imc = peso / (alt ** 2)
print(f'Seu IMC é de: {imc:.1f}\nVocê está ', end='')
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obeso(a)')
else:
    print('Obesidade mórbida')
