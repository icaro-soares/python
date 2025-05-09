#Ler altura e largura de uma parede, calcular a área, saber qntd de tinta p/ pintar 1l = 2m

altura = float(input('Qual a altura da parede (m)? '))
largura = float(input('Qual a largura da parede (m)? '))
area = altura * largura
litros = area/2
print(f'A sua parede, de {largura}x{altura} tem {area:.2f}m².\nSerão necessários {litros:.1f}l de tinta para pintá-la.')