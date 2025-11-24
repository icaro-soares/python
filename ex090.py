ficha = {}
ficha['aluno'] = str(input('Nome do(a) aluno(a): ')).strip()
ficha['média'] = float(input('Média do(a) aluno(a): '))
if ficha['média'] >= 7:
    ficha['situação'] = 'Aprovado(a)'
elif 5 <= ficha['média'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado(a)'
print('-='*30)
for k, v in ficha.items():
    print(f'• {k} -> {v}')