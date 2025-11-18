from random import randint


lista = []
jogos = int(input('Quantos jogos devo gerar: '))
cont = 0
while cont <= jogos:
    for c in range(0, 6):
        num = randint(0, 61)
        while num not in lista:
            lista.append(num)
    print(lista)
   
