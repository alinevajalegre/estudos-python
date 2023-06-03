"""
leia um num inteiro e diga se é ou não um numero primo
"""

number = int(input("Digite um num: "))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(number, 'não é primo')
            break
    else:
        print(number, 'é primo')