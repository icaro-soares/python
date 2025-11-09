geral = []
pessoas = []
p_quilo = []
while True:
    nome = str(input('Qual o nome: ')).title().strip()
    pessoas.append(nome)
    peso = float(input('Qual o peso [kg]: '))
    p_quilo.append(peso)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar [S/N]? ')).strip()[0]
    if continuar in 'Nn':
        break
geral.append(pessoas)
geral.append(p_quilo)
print(f'Pessoas cadastradas: {len(pessoas)}')
print(p_quilo)
