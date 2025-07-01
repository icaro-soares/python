#Crie um programa que leia a altura e largura de uma parede em metros, calcule a área e quanto de tinta será necessário para pintá-la, sabendo que cada 1l de tinta pinta 2m²


alt = float(input('Qual a altura da parede (m): '))
lar = float(input('Qual a largura da parede (m): '))
area = alt * lar
tinta_necessaria = area/2
print(f'A área da parede é {area}m²\nE serão necessários {tinta_necessaria}L de tinta para pintar a parede')

