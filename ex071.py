valor = int(input('Qual valor deseja sacar? R$'))
total = valor
cédula = 50
total_cédula = 0
while True:
    if total >= cédula:
        total-=cédula
        total_cédula+=1
    else:
        if total_cédula > 0:
            print(f'Total de {total_cédula} cédulas de R${cédula}')
        if cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula ==10:
            cédula = 5
        elif cédula == 5:
            cédula = 1
        total_cédula = 0
        if cédula == 0:
            break