from random import randint
lista = []
jogos = []
tot = 1
qnt = int(input('Quantos jogos devo gerar? '))
while tot <= qnt:
    c = 0
    while True:
        n = randint(0, 60)
        if n not in lista:
            lista.append(n)
            c+=1
        if c >= 6:
            break
    jogos.append(sorted(lista)[:])
    lista.clear()
    tot+=1
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')