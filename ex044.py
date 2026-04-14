preço = float(input('Preço: R$'))
opc = int(input('''Escolha a forma de pagamento:
                [1 - à vista dinheiro/cheque: 10% desconto]
                [2 - à vista no cartão: 5% de desconto]
                [3 - em até 2x no cartão: preço normal]
                [4 - 3x ou mais no cartão]: 20% de juros: '''))
if opc == 1:
    novo_preço = preço - (preço * 0.10)
    print(f'Seu produto com 10% de custará R${novo_preço:.2f}')
elif opc == 2:
    novo_preço = preço - (preço * 0.05)
    print(f'Seu produto com 5% de desconto custará R${novo_preço:.2f}')
elif opc == 3:
    parc = int(input('Em quantas parelas que dividir: '))
    valor_parc = preço / parc
    print(f'Serão {parc}x de R${valor_parc:.2f}')
elif opc == 4:
    parc = int(input('Em quantas parcelas quer dividir: '))
    novo_preço = preço + (preço * 0.20)
    valor_parc = novo_preço / parc
    print(f'''O preço será R${novo_preço:.2f} e serão {parc}x de R${valor_parc:.2f}''')
else:
    print('Opção inválida, tente novamente!')
