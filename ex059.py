
funcionando = True
n1 = int(input('Insira o 1º valor: '))
n2 = int(input('Insira o 2º valor: '))
opção = int(input('Escolha a operação a ser realizada [1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
while funcionando:
    match opção:
        case 1:
            print('Opção escolhida ADIÇÃO')
            soma = n1 + n2
            print(f'{n1} + {n2} = {soma}')
        case 2:
            print('Opção escolhida SUBTRAÇÃO')
            sub = n1 - n2
            print(f'{n1} - {n2} = {sub}')
        case 3:
            print('Opção escolhida MULTIPLICAÇÃO')
            multi = n1 * n2
            print(f'{n1} x {n2} = {multi}')
        case 4:
            print('Opção escolhida DIVISÃO')
            div = n1 / n2
            print(f'{n1}: {n2} = {div}')
        case 6:
            funcionando = False
            print('Obrigado por usar a calculadora!')
        