from random import randint
v = 0
while True:
    cpu_n = randint(0, 10)
    n = int(input('Escolha do P1: '))
    while n < 0:
        print('Valor inválido, digite novamente!')
        n = int(input('Digite um valor: '))

    jogador = str(input('Escolha par ou ímpar [P/I]: ')).strip()[0]
    while jogador not in 'PpIi':
        print('Dado inválido, por favor, tente novamente.')
        jogador = str(input('Escolha par ou ímpar [P/I]: ')).strip()[0]

    soma = n + cpu_n

    if soma%2==0 and jogador in 'Pp':
        print('O P1 venceu!')
        v+=1
    elif soma%2!=0 and jogador in 'Ii':
        print('O P1 venceu!')
        v+=1
    elif soma%2==0 and jogador not in 'Pp':
        print('Cpu venceu!')
    elif soma%2!=0 and jogador not in 'Ii':
        print('Cpu venceu!')

    continuar = str(input('Quer continuar [S/N]: ')).strip()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]: ')).strip()[0]
    if continuar in 'Nn':
        break

print(f'O J1 teve {v} vitórias')