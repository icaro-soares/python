#Crie um programa que leia um valor em metros e mostre o valor em cm e mm


m = float(input('Digite um valor (m): '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print(f'O valor em metros foi: {m}m')
print(f'{km}km\n{hm}hm\n{dam}dam\n{dm}dm\n{cm}cm\n{mm}mm')