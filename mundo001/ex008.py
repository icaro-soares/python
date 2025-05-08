print('Conversor de Medidas\n'.upper())
n = int(input('Digite um valor de distância (m): '))

n_km = n/1000
n_hm = n/100
n_dm = n/10
n_dm = n*10
n_cm = n*100
n_mm = n*1000

print(f'{n_km}km\n{n_hm}hm\n{n}m\n{n_dm}dm\n{n_cm}cm\n{n_mm}mm')
