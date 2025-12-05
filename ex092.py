from datetime import date


dados = {}
dados['nome'] = str(input('Nome: '))
dados['nasc'] = int(input('Nascimento: '))
dados['idade'] = date.today().year - dados['nasc']
dados['ct'] = int(input('Nº da CT (0 não existe): '))
if dados['ct'] != 0:
    dados['salario'] = float(input('Salário: R$'))
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 65) - date.today().year)
print('-='*30)
for k, v in dados.items():
    print(f'{k}: {v}')
