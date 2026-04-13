from random import shuffle


alunos = []
for c in range(0, 4):
    n = str(input(f'{c+1}º aluno: '))
    alunos.append(n)
shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
