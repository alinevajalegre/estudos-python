
"""
faça uma tabuada de um numero que o usuario escolher utilizando laço for
"""

numero = int(input("Qual o número para a tabuada? "))

for n in range(11):
    linha = numero * n
    print("{} * {} = {}".format(numero, n, linha))

