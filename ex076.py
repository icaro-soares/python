lista_comidas = ('Sonho de Padaria', 2.50,
                 'Croissant', 3.00,
                 'Pão Doce', 2.50,
                 'Pizza', 10.00,
                 'Guaraná', 5.00,
                 'Queijadinha', 3.50,
                 'Bolacha', 4.00,
                 'Pudim', 5.00)
print('Cardápio'.upper().center(40))
print('-'*40)
for pos in range(0, len(lista_comidas)):
    if pos%2==0:
        print(f'{lista_comidas[pos]:.<30}', end='')
    else:
        print(f'R${lista_comidas[pos]:>7.2f}'.replace('.', ','))
print('-'*40)
