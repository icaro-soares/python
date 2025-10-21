
funcionando = True
n1 = int(input('Insira o 1º valor: '))
n2 = int(input('Insira o 2º valor: '))
opção = int(input('[1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
while funcionando:
    match opção:
        case 1:
            print('Opção escolhida ADIÇÃO')
            soma = n1 + n2
            print(f'{n1} + {n2} = {soma}')
            print('='*20)
            opção = int(input('[1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
        case 2:
            print('Opção escolhida SUBTRAÇÃO')
            sub = n1 - n2
            print(f'{n1} - {n2} = {sub}')
            print('='*20)
            opção = int(input('[1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
        case 3:
            print('Opção escolhida MULTIPLICAÇÃO')
            multi = n1 * n2
            print(f'{n1} x {n2} = {multi}')
            print('='*20)
            opção = int(input('[1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
        case 4:
            print('Opção escolhida DIVISÃO')
            div = n1 / n2
            print(f'{n1}: {n2} = {div}')
            print('='*20)
            opção = int(input('[1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
        case 5:
            print('Opção escolhida NOVOS VALORES')
            n1 = int(input('Insira o 1º valor: '))
            n2 = int(input('Insira o 2º valor: '))
            opção = int(input('[1 - Adição][2 - Subtração][3 - Multiplicação][4 - Divisão][5 - Novos Valores][6 - Sair]: '))
        case 6:
            print('Obrigado por usar a calculadora!')
            funcionando = False
            
        