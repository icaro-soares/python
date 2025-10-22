n = int(input('Quantos termos da sequência de Fibonacci devo mostrar: '))
t1 = 0
t2 = 1
c = 3
print(t1, end=' → ')
print(t2, end=' → ')
while c <= n:
    t3 = t1 + t2
    print(t3, end=' → ')
    t1 = t2
    t2 = t3
    c+=1
print('ACABOU!')