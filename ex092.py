from datetime import date


ano_atual = date.today().year
carteira_trabalho = {}
carteira_trabalho['nome'] = str(input('Nome: ')).strip().title()
carteira_trabalho['ano_nascimento'] = int(input('Ano de nascimento: '))
carteira_trabalho['idade'] = ano_atual - carteira_trabalho['ano_nascimento']
carteira_trabalho['salário'] = float(input('Qual seu salário? R$'))
carteira_trabalho['número_ct'] = int(input('Nº da CT [0 não existe]: '))
if carteira_trabalho['número_ct'] <= 0:
    carteira_trabalho['número_ct'] = 'Não tem CT'
carteira_trabalho['ano_contratação'] = int(input('Em que ano foi contratado(a)? '))
carteira_trabalho['idade_contratação'] = carteira_trabalho['ano_contratação'] - carteira_trabalho['ano_nascimento']
print('-='*30)
for k, v in carteira_trabalho.items():
    print(f'{k}: {v}')
