#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input('Digite um valor (m): '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm=m*1000
print(f'Seu valor convertido:\nkm: {km}\nhm: {hm}\ndam: {dam}\nm: {m}\ndm: {dm}\ncm: {cm}\nmm: {mm}')
