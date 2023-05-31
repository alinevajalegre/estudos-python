"""
Escreva um programa que pergunte o salario de um
funcionario e calcule o valor do seu aumento.
Para salarios superiores a 1250 calcule um aumento de
10%. Para inferiores ou iguais, o aumento é de 15%
"""

salario = float(input("Qual o salario? "))

if salario > 1250:
    novo_salario = salario + ((salario * 10)/100)
    print('Aumento de 10%, novo salario {:.2f}'.format(novo_salario))
else:
    novo_salario = salario + ((salario * 15)/100)
    print('Aumento de 15%, novo salario {:.2f} '.format(novo_salario))