#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
# ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorridos = float(input('Qual a quantidade de KM percorridos?'))
qnt_dias = int(input('Qual a quantidade de dias?'))
valor_dias = qnt_dias * 60
valor_km = km_percorridos * 0.15
valor_total = valor_dias + valor_km
print('O valor total a pagar é R${:.2f}'.format(valor_total))
