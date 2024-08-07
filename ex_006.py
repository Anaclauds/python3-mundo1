#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

numero = int(input('Insira um número: '))
print('O dobro do seu número é {}'.format(numero*2))
print('O triplo do seu número é {}'.format(numero*3))

raiz_quadrada = math.sqrt(numero)

print('A raíz quadrada do seu número é {}'.format(raiz_quadrada))

#outra forma de fazer a raíz quadrada
numero = int(input('Insira um número: '))
raiz_q = numero ** (1/2)

print('A raíz quadrada de {} é {:.1f}'.format(numero, raiz_q))
