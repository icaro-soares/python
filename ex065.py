soma = cont = maior = menor = 0
while True:
    n = int(input('Digite um valor: '))
    soma+=n
    cont+=1
    media = soma/cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Devo continuar [S/N]: ')).strip()[0]
    while resp not in 'SsNn':
        print('Resposta inválida!')
        resp = str(input('Devo continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        print('='*20)
        break
print(f'Foram digitados {cont} valores\nA soma dos valores é {soma}\nA média entre eles é {media}')
print(f'O maior valor foi {maior}\nO menor valor foi {menor}')
