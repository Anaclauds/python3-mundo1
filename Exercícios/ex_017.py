#Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retangulo
#calcule e mostre o comprimento da hipotenusa

#exemplo sem importação da classe math
'''co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

#exemplo com importação da classe
from math import hypot #se importa dessa maneira, posteriormente não precisa referenciar math no código novamente
co = float(input('Comprimento do cateto oporto: '))
ca = float(input('Comprimento do cateto adjascente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
