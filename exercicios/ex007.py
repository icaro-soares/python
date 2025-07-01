#Leia duas notas de um aluno pelo teclado e mostre a média entre elas


nota1 = float(input('Digite a 1ª nota do aluno: '))
nota2 = float(input('Digite a 2ª nota do aluno: '))
media = (nota1+nota2)/2
print(f'O aluno teve as notas {nota1:.1f} e {nota2:.1f}.\nSua média final foi {media:.1f}')