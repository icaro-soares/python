lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        print('Fim do programa!')
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
