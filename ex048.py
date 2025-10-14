soma = 0
n = 0
for cont in range(1, 501):
    if cont%3==0 and cont%2!=0:
        print(cont, end=' > ')
        n+=1
        soma+=cont
print('Acabou!')
print(f'A soma dos números ímpares e múltiplos de entre os {n} números é {soma}')