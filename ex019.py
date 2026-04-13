from random import choice


alunos = []
for c in range(0, 4):
    n = str(input(f'{c+1}º aluno(a): '))
    alunos.append(n)
print(f'O aluno escolhido para apagar o quadro foi {choice(alunos)}')
