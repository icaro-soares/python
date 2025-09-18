#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
graus_celsius = float(input('Digite a temperatura atual em graus celsius: '))
#fórmula: (graus_celsius*9/5) + 32
graus_farenheit = (graus_celsius*9/5) + 32
print(f'A temperatura em graus celsius {graus_celsius}°, equivale a {graus_farenheit}° farenheit')
