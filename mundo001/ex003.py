def soma(n1, n2):
    s = n1 + n2
    return f'A soma entre {n1} e {n2} é {s}'


x1 = int(input('Digite um valor: '))
x2 = int(input('Digite outro valor: '))
tot = soma(x1, x2)
print(tot)
