cont = 0
print('Tabuada\n')
n = int(input('Qual número você quer saber a tabuada: '))
print(f'Tabuada de {n}'.upper())
print('-'*20)
while (cont <= 10):
    print(f'{n} x {cont:2} = {n*cont:2}')
    cont+=1
print('-'*20)
