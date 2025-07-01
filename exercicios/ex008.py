#Escreva um programa que leia uma medida em metros e mostre o valor em km, hm, dam, cm, dm, mm


metros = float(input('Digite um medida (m): '))
km = metros/1000
hm = metros/100
dam = metros/10
dm = metros*10
cm = metros*100
mm = metros*1000
print(f'A medida em metros foi {metros}m\n{km}km\n{hm}hm\n{dam}dam\n{cm}cm')

