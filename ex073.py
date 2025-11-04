times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Fluminense',
 'Botafogo', 'Vasco da Gama', 'São Paulo', 'Corinthians', 'Grêmio', 'Bragantino'
 , 'Atlético-MG', 'Ceará SC', 'Internacional', 'Santos', 'EC Vitória', 
 'Fortaleza', 'Juventude', 'Sport Recife')

#Cinco primeiros
c = 0
for time in range(0, 4):
    print(f'{c+1}º lugar: {times[time]}')
    c+=1
print('='*20)
#Quatro últimos times
c = 17
for time in range(-4, 0):
    print(f'{c}º lugar: {times[time]}')
    c+=1
#Times em ordem alfabética
print('='*20)
print(sorted(times))
print('='*20)
#Posição do 'Vasco da Gama'
print(f'O time Vasco da Gama está em {times.index('Vasco da Gama')+1}º lugar')
