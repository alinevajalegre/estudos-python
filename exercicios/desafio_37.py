"""
Escreva um programa que leia um num inteiro qualquer e peca
para o usuario escolher qual sera a base de conversao:
1 para binario
2 para octal
3 para hexadecimal
"""

inteiro = int(input('Digite um num inteiro '))
escolha = int(input('Digite:\n 1 para binario\n 2 para octal\n 3 para hexadecimal '))

if escolha == 1:
    print('transformar para binario')
elif escolha == 2:
    print('transformar para octal')
else:
    print('transformar para hexa')
