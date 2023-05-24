"""
Escreva um programa que pergunte a qtd de km percorridos por um carro alugado e a qtd de dias
pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado
"""

kms = float(input('Quantos kms percorridos? \n'))
dias = int(input('Quantos dias ele foi alugado? \n'))

preco = (60 * dias) + (0.15 * kms)

print('O preco total é ',preco)