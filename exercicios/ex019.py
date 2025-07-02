#Crie um programa que faça o sorteio de um aluno de uma lista de 4 alunos
from random import choice


aluno1 = str(input('Digite o nome do 1º aluno(a): '))
aluno2 = str(input('Digite o nome do 2º aluno(a): '))
aluno3 = str(input('Digite o nome do 3º aluno(a): '))
aluno4 = str(input('Digite o nome do 4º aluno(a): '))
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'Aluno sorteado: {choice(lista)}')