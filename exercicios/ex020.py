#Um professor quer sortear o nome de um dos alunos do exercício anterior para apresentar um trabalho, crie um programa que faça isso para ele
from random import choice


aluno1 = str(input('Digite o nome do 1º aluno(a): '))
aluno2 = str(input('Digite o nome do 2º aluno(a): '))
aluno3 = str(input('Digite o nome do 3º aluno(a): '))
aluno4 = str(input('Digite o nome do 4º aluno(a): '))
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno que vai apresentar o trabalho é o(a): {choice(lista)}')