"""
    Crie um programa que leia o nome completo e retorne:
    1- o nome com todas as letras maiusculas
    2- o nome com todas minusculas
    3- quantas letras ao todo (sem considerar espacos)
    4- quantas letras tem o primeiro nome
"""

nome_completo = input('Qual seu nome completo? ')

#1
print('Nome todo maiusculo -> ', nome_completo.upper())

#2
print('Nome todo minusculo -> ', nome_completo.lower())

#3
nome_completo_sem_espacos = nome_completo.replace(' ', '')
print('Quantas letras ao todo -> ', len(nome_completo_sem_espacos))

#4
nome_splitted = nome_completo.split()
print(len(nome_splitted[0]))
