from math import sqrt, hypot


cateto_oposto = float(input('Diga qual o cateto adjacente (cm): '))
cateto_adjacente = float(input('Digite o cateto oposto (cm): '))
#hipotenusa² = (cateto_oposto²) + (cateto_adjacente²)
hipotenusa = sqrt((cateto_oposto**2) + (cateto_adjacente**2))
print(f'A hipotenusa do triângulo retângulo acima é de {hipotenusa:.2f}cm²')
#utilizando função interna
hipo = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa, utilizando a função interna é: {hipo:.2f}cm²')
