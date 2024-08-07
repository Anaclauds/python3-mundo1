#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
valor = float(input('Insira um valor: '))
valor_centimetros = valor*100
valor_milimetros = valor*1000
print('Conversão em centímetros: {}'.format(valor_centimetros))
print('Conversão em milímetros: {}'.format((valor_milimetros)))

