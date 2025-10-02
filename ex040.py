'''
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''
nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
média = (nota1 + nota2)/2
print(f'Sua média foi {média:.1f}'.replace('.', ','))
if média >= 7.0:
    print('Aluno APROVADO')
elif 5.0 <= média <= 6.9:
    print('Aluno de RECUPERAÇÃO')
else:
    print('Aluno REPROVADO')

#media >= 5.0 and média <= 6.9
#5.0 <= media <= 6.9