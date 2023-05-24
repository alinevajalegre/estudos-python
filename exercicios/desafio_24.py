"""
crie um programa que leia o nome de uma cidade
e diga se ela comeca ou nao com o nome "santo"
"""

nome = input('Nome da cidade: ')

if nome[0:5] == 'Santo':
    print('Comeca com santo')
else:
    print('Nao comeca com santo')
