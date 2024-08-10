"""Faça um programa que leia três números e mostre qual é o maior e qual é o menor"""
n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
print('Os três números escolhidos foram: {}, {}, {}'.format(n1, n2, n3))
if (n1 > n2) and (n1 > n3):
    print('{} é o maior número!'.format(n1))
if (n2 > n1) and (n2 > n3):
    print('{} é o maior número!'.format(n2))
if (n3 > n1) and (n3 > n2):
    print('{} é o maior número!'.format(n3))
if (n1 < n2) and (n2 < n3):
    print('{} é o menor número!'.format(n1))
if (n2 < n1) and (n2 < n3):
    print('{} é o menor número!'.format(n2))
if (n3 < n1) and (n3 < n2):
    print('{} é o menor número!'.format(n3))

"""forma mais simplificada nas condições:
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    menor = b
if c > a and c > b:
    maior = c"""