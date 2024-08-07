#Crie um código que tranforme ºC em ºF
temperatura_celsius = float(input('Insira a temperatura em ºC: '))
temperatura_fahrenheit = ((temperatura_celsius * 9)/5) + 32
#nesse caso, pela ordem de procedencia daria para executar sem parenteses
print('A temperatura {}ºC é equivalente a {}ºF'.format(temperatura_celsius, temperatura_fahrenheit))
