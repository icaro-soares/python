#Crie um programa que converta C° para F°


grau_celsius = float(input('Digite um temperatura em graus celsius: '))
fahrenheit = (grau_celsius * 9/5) + 32
print(f'A temperatura é {grau_celsius:.1f}°C\nEssa temperatura convertida em graus fahrenheit é {fahrenheit}°F')