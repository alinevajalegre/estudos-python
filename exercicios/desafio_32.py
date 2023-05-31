"""
Faca um programa que leia um ano qualquer
e mostre se ele é bissexto
"""

#os anos bissextos são aqueles múltiplos de 4, ou seja, a cada quatro anos temos um ano bissexto.

ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é bissexto')