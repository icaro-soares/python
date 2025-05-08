print('Escola Javali Cansado\nBoletim de notas\n'.upper())
aluno = str(input('Nome do aluno: '))
nota1 = float(input('Nota da AV1: '))
nota2 = float(input('Nota da AV2: '))
media = (nota1+nota2)/2
print(f'A média final do aluno {aluno} foi de {media:.1f}.')
