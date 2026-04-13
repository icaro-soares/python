from math import sin, cos, tan, radians


ang = float(input('Digite o ângulo: '))
print(f'O ângulo {ang}° tem o SENO de {sin(radians(ang)):.2f}')
print(f'O ângulo {ang}° tem o COSSENO de {cos(radians(ang)):.2f}')
print(f'O ângulo {ang}° tem a TANGENTE de {tan(radians(ang)):.2f}')
