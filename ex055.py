maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c}ª pessoa (kg): '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi {maior:.1f}kg')
print(f'O menor peso foi {menor:.1f}kg')