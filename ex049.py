#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(0, 11):
    print(f'{c:2} x {n:3} = {c*n:3}')
