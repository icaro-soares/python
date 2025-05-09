from math import trunc


n = float(input('Digite um número real qualquer: '))
parte_inteira = int(n) #Mostra apenas a parte inteira do número
print(f'O número digitado foi {n}')
print(f'Sua parte inteira é {parte_inteira}')
print(f'A sua parte inteira é {n:.0f}') #arredonda para o valor mais próximo
print(f'A parte inteira: {trunc(n)}') #usa a função trunc() importada da biblioteca math
