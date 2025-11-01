número_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                   'onze', 'doze', 'treze','quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


n = int(input('Digite um valor para vê-lo escrito por extenso [0 a 20]: '))
if n not in range(len(número_extenso)):
    print('Valor inválido! Reinicie o programa!')
    exit()
print(f'Você digitou: {número_extenso[n].title()}')