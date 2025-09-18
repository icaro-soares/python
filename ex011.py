#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Qual a largura da parede (m): '))
altura = float(input('Qual a altura da parede (m): '))
area = largura*altura
quantidade_tinta = area/2
print(f'A sua parede tem área de {area:.2f}m². Serão necessários {quantidade_tinta} litros para pintá-la.')
