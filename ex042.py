'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
seg1 = int(input('Qual a medida do 1º segmento? '))
seg2 = int(input('Qual a medida do 2º segmento? '))
seg3 = int(input('Qual a medida do 3º segmento? '))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Pode formar um triângulo!')
    if seg1 == seg2 == seg3:
        print('Triângulo Equilátero')
    elif seg1 == seg2 or seg1 == seg3:
        print('Triângulo Isóceles')
    else:
        print('Triângulo Escaleno')
else:
    print('Não pode formar um triângulo')