from random import randint


v = 0
while True:
    jogador = int(input('Digite um valor [entre 0 e 10]: '))
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/Í]: ')).strip().upper()[0]
    cpu = randint(0, 10)
    soma = jogador + cpu
    par = soma%2==0
    print(f'Jogador jogou: {jogador}; Computador jogou: {cpu}; Total {soma}')
    if soma%2==0:
        print('Deu PAR')
    else:
        print('Deu ÍMPAR')
    if tipo == 'P':
        if par:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if not par:
            print('Você venceu!')
            v+=1
        else:
            print('Você perdeu!')
            break
print(f'Game Over! Você conseguiu {v} vitórias')
