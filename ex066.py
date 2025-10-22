soma = 0
while True:
    n = int(input('Digite um valor [9999 p/ parar]: '))
    if n == 9999:
        break
    soma+=n
print(f'A soma dos valores é {soma}')