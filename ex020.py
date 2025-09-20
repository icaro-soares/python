from random import choices


#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
aluno_um = str(input('Digite o nome do 1º aluno(a): '))
aluno_dois = str(input('Digite o nome do 2º aluno(a): '))
aluno_três = str(input('Digite o nome do 3º aluno(a): '))
aluno_quatro = str(input('Digite o nome do 4º aluno(a): '))
lista_alunos = [aluno_um, aluno_dois, aluno_três, aluno_quatro]
ordem_alunos = choices(lista_alunos)
print(ordem_alunos)
