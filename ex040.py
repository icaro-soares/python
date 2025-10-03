'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
n1 = float(input('Digite a 1ª nota do(a) aluno(a): '))
n2 = float(input('Digite a 2ª nota do(a) aluno(a): '))
m = (n1+n2)/2
print(f'Sua média final foi {m:.1f}')
if m < 5:
    print('ALUNO(A) REPROVADO(A)')
elif 5 <= m <= 6.9:
    print('ALUNO(A) DE RECUPERAÇÃO')
else:
    print('ALUNO(A) APROVADO(A)')