#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario = float(input('Insira o salário: '))
salario_com_aumento = salario + ((15/100)*salario)

print('O novo salário é:R${:.2f}'.format(salario_com_aumento))