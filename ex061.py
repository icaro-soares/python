primeiro = int(input('Qual o primeiro termo da PA: '))
razão = int(input('Qual a razão da PA: '))
décimo = primeiro + (11 - 1) * razão
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end=' => ')
    termo += razão
    cont += 1
print('ACABOU')