pessoas = []
while True:
    nome = str(input('Qual o nome: ')).title().strip()
    pessoas.append(nome)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]? ')).strip()[0]
    if continuar in 'Nn':
        break
