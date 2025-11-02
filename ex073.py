c = 0
times = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Fluminense',
 'Botafogo', 'Vasco da Gama', 'São Paulo', 'Corinthians', 'Grêmio', 'Bragantino'
 , 'Atlético-MG', 'Ceará SC', 'Internacional', 'Santos', 'EC Vitória', 
 'Fortaleza', 'Juventude', 'Sport Recife')

for time in range(0, 5):
    print(f'{c+1}º lugar: {times[time]}')
    c+=1
print('='*20)

print('='*20)
print(sorted(times))
print('='*20)
