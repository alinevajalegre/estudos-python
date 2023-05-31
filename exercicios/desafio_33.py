"""
 Faca um programa que leia tres numeros
 e mostre qual é o maior e qual é o menor
"""

num1 = int(input("Primeiro num "))
num2 = int(input("Segundo num "))
num3 = int(input("Terceiro num "))

lista_num = [num1, num2, num3]

print('Maior numero -> ', max(lista_num))
print('Menor numero -> ', min(lista_num))
