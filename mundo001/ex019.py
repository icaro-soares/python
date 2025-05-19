from random import choice


aluno_um = str(input('Digite o nome do(a) 1º aluno(a): '))
aluno_dois = str(input('Digite o nome do(a) 2º aluno(a): '))
aluno_tres = str(input('Digite o nome do(a) 3º aluno(a): '))
aluno_quatro = str(input('Digite o nome do(a) 4º aluno(a): '))
alunos = [aluno_um, aluno_dois, aluno_tres, aluno_quatro]

print(f'O(A) aluno(a) sorteado(a) foi: {choice(alunos)}')
