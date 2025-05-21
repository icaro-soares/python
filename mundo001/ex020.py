from random import shuffle


aluno_um = str(input('Digite o nome do primeiro aluno: '))
aluno_dois = str(input('Digite o nome do segundo aluno: '))
aluno_tres = str(input('Digite o nome do terceiro aluno: '))
aluno_quatro = str(input('Digite o nome do quarto aluno: '))
lista = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]
shuffle(lista)
print(f'A ordem de apresentção será {lista}')
