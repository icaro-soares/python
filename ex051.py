primeiro = int(input('Digite o primeiro termo de uma PA: '))
razão = int(input('Qual vai ser a razão? '))
décimo_termo = primeiro + (11 - 1) * razão
for cont in range(primeiro, décimo_termo, razão):
    print(cont, end=' > ')
print('Acabou!')