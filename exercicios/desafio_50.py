"""
programa que leia 6 numeros inteiros e mostre a soma apenas daqueles
que forem pares. se o valor digitado for impar, desconsidere-o.
"""
soma = 0

for i in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num

print("soma dos n elementos pares dentro dos 6 numeros: ", soma)
