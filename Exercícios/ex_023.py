"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígidos separados
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar 1

Testando de forma matematica"""

numero = int(input('Digite um número de 0 a 9999: '))
u = numero//1 % 10
d = numero//10 % 10
c = numero//100 % 10
m = numero//1000 % 10
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))





