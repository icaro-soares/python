from math import radians, sin, cos, tan


ang = float(input('Digite o ângulo que você quer (cm): '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print(f'SENO: {s:.2f}°\nCOSSENO: {c:.2f}°\nTANGENTE: {t:.2f}°')
