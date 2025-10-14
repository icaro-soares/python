cont = 0
soma = 0
for c in range(1, 7):
    n = int(input('Digite um valor: '))
    if n%2==0:
        soma+=n
        cont+=1
print(f'Foram digitados {cont} valores PARES e a soma é {soma}')