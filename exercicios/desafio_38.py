"""
escreva um programa que leia dois numeros inteiros e compare-os,
mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- nao existe valor maior, os dois sao iguais
"""

num1 = int(input("Digite o primeiro num "))
num2 = int(input("Digite o segundo num "))

if num1 > num2:
    print("o primeiro valor é maior")
elif num1 < num2:
    print("o segundo valor é maior")
elif num1 == num2:
    print("nao existe valor maior, os doiss sao iguais")
else:
    print("Invalido")