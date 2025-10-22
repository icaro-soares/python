while True:
    n = int(input('Valor para tabuada [digite um valor negativo p/ parar]: '))
    if n < 0:
        break
    cont = 0
    print(f'Tabuada de {n}'.center(25))
    print('='*25)
    while cont <= 10:
        print(f'{cont:2} x {n} = {cont*n:3}')
        cont+=1
    print('='*25)
