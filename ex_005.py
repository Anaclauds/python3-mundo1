#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e antecessor
numero = int(input('Insira um número: '))
print('O sucessor de {} é {}, e o antecessor é {}'.format(numero, (numero+1), (numero-1)))

#outra forma
numero = int(input('Insira um número: '))
sucessor = numero + 1
antecessor = numero - 1
print('Nesta outra forma de fazer:\n O sucessor de {} é {}, e o seu antecessor é {}'.format(numero, sucessor, antecessor))
