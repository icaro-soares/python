#Ler o salário e mostrar novo salário com 15% de aumento
salario = float(input('Qual seu salário atual? R$'))
print(f'Seu salário é de R${salario:.2f}'.replace('.', ','))
aumento = salario*15/100
novo_salario = salario + aumento
print(f'Seu novo salário é de R${novo_salario:.2f}'.replace('.', ','))
