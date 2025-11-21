lista_boletim = []
while True:
    nome = str(input('Nome do(a) aluno(a): ')).title().strip()
    n1 = float(input('1ª nota do(a) aluno(a): '))
    n2 = float(input('2ª nota do(a) aluno(a): '))
    m = (n1+n2)/2
    lista_boletim.append([nome, [n1, n2], m])
    resp = str(input('Quer continuar [S/N]? ')).strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(lista_boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True: 
    print('-'*35)
    opc = int(input('Mostrar notas de que aluno [999 p/ parar]? '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(lista_boletim) - 1:
        print(f'Notas de {lista_boletim[opc][0]}: {lista_boletim[opc][1]}')
print('<< VOLTE SEMPRE >>')