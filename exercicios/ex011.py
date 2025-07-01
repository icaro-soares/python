#Faça um programa que leia a Altura e a Largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que 1l de tinta pinta 2m da parede


altura = float(input('Altura da parede (m): '))
largura = float(input('Largura da parede (m): '))
area_parede = altura*largura
print(f'Sua parede tem área de {area_parede:.2f}m²')
tinta_necessaria = area_parede/2
print(f'Serão necessários {tinta_necessaria:.1f} litros para pintar a parede')
