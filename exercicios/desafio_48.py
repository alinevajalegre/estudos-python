"""
calcule a soma entre todos os numeros impares que
sao multiplos de 3 e que se encontram no intervalo de 1 até 500
"""
add = 0

for number in range(1, 500):
    if number % 2 != 0:
        if number % 3 == 0:
            add = number + add
print(add)