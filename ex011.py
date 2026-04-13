larg = float(input('Largura (m): '))
alt = float(input('Altura (m): '))
a = larg * alt
print(f'Sua parede tem área de {a:.2f}m²')
l = a/2
print(f'Sabendo que 1L de tinta pintam 2m² de área, serão necessários {l}L para pintar toda parede.')