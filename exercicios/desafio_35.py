"""
Desenvolva um programa que leia o comprimento de 3
retas e diga ao usuario se elas podem ou nao
formar um triangulo
"""

num1 = int(input("Lado 1: "))
num2 = int(input("Lado 2: "))
num3 = int(input("Lado 3: "))

if num1 < (num2 + num3) and num2 < (num1 + num3) and num3 < (num1 + num2):
    print("Os segmentos podem formar um triangulo")
else:
    print("Os segmentos NAO podem formar um triangulo")