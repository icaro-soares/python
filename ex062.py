primeiro = int(input('Qual o primeiro termo da PA: '))
razão = int(input('Qual a razão: '))
décimo = primeiro + (11 - 1) * razão
termo = primeiro
c = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, end=' => ')
        termo+=razão
        c+=1
    print('PAUSA')
    mais = int(input('Mais quantos termos devo mostrar: '))
print('ACABOU!')