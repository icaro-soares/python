from random import choice
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
aluno_um = str(input('Nome do 1º aluno(a): '))
aluno_dois = str(input('Nome do 2º aluno(a): '))
aluno_três = str(input('Nome do 3º aluno(a): '))
aluno_quatro = str(input('Nome do 4º aluno(a): '))
lista_alunos = [aluno_um, aluno_dois, aluno_três, aluno_quatro]
aluno_escolhido = choice(lista_alunos)
print(f'O aluno escolhido para apagar o quadro foi: {aluno_escolhido}')
