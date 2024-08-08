"""Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO" """
cidade = str(input('Qual o nome da sua cidade?: ')).strip() #para remover os espaços antes e depois
print(cidade[:5].upper() == 'SANTO') #Pega da primeira posição até a quinta e verifica se é igual a santo
#upper para deixar tudo maiúsculo para a comparação