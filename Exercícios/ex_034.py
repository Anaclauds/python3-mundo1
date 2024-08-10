"""Escreva um programa que pergunte o salário de funcionários e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%"""

salario = float(input('Insira seu salário: '))
if salario > 1250.00:
    aumento = (salario/100)*10
    salario_aumentado = salario + aumento
    print('Valor do novo salário: {}'.format(salario_aumentado))
else:
    aumento = (salario/100)*15
    salario_aumentado = salario + aumento
    print('Valor do novo salário: {}'.format(salario_aumentado))
