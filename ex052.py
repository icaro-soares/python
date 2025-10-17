n = int(input('Digite um número qualquer: '))
tot = 0
for c in range(1, n+1):
    if n%c==0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\n\033[mO número foi divisível por {tot} valores')
if tot == 2:
    print('O número é primo')
else:
    print('O número não é primo')