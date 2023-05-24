"""
faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o
primeiro e o ultimo nome separadamente

ex: ana maria de souza
primeiro = ana
ultimo = souza
"""

nome = input('Nome completo: ')
nome_separado = nome.split()

print('Primeiro nome -> ', nome_separado[0])
print('Ultimo nome -> ', nome_separado[-1])

