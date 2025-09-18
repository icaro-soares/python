#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite a 1ª nota do aluno: '))
n2 = float(input('Digite a 2ª nota do aluno: '))
media = (n1+n2)/2
print(f'O aluno que tirou as notas {n1} e {n2} teve média {media:.1f}')
