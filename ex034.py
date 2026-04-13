sal = float(input('Digite seu salário: R$'))
if sal > 1_250:
    sal = sal + (sal * 0.10)
else:
    sal = sal + (sal * 0.15)
print(f'Com o aumento seu salário será de {sal:.2f}')
