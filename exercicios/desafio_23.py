"""
Faca um programa que leia um numero de 0 a 9999 e mostre
na tela cada um dos digitos separados

ex: numero 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
"""

num = int(input('Digite um num de 0 a 9999'))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('Unidade', unidade)
print('Dezena', dezena)
print('Centena', centena)
print('Milhar', milhar)