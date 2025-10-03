'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
r1 = int(input('Qual o tamanho do 1º segmento: '))
r2 = int(input('Qual o tamanho do 2º segmento: '))
r3 = int(input('Qual o tamanho do 3º segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo')
    if r1 == r2 == r3:
        print('Triângulo EQUILÁTERO')
    elif r1 != r2 != r3:
        print('Triângulo ESCALENO')
    else:
        print('Triângulo ISÓCELES')
else:
    print('Não pode formar um triângulo')