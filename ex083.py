expr = str(input('Digite uma expressão matemática: ')).strip()
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
