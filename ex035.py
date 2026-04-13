r1 = float(input('1º lado: '))
r2 = float(input('2º lado: '))
r3 = float(input('3º lado: '))
# a soma dos dois lados não pode ser maior que o terceiro
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo!')
else:
    print('Nao pode formar um triângulo!')
