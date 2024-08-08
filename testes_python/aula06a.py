#Descobrindo o tipo primitivo
"""n1 = input('Digite um valor: ')
print('O tipo primitivo é: ', type(n1)) #pedindo para mostrar o tipo primitivo utilizando type
#não é o correto, pois se não envolver no imput, ele entederá que é uma string(str)"""

#Correto:
"""n1 = int(input('Digite um valor: '))
print('O tipo primitivo é: ', type(n1))"""

## Somando e mostrando os valores inseridos no resultado
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
resultado = n1+ n2
#print('A soma entre', n1, ' e ', n2, ' é:', resultado)
##print de outro jeito
print('A soma entre {} e {} vale {}'.format(n1,n2,resultado))

