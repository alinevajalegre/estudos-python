
"""
if simples
"""
valor = 10

if valor > 6:
    print('O valor é maior que 6')

if True:
    print("Este bloco vai ser sempre executado")

"""
if else
"""

idade = 16

if idade < 17:
    print('A idade é MENOR que 17')
else:
    print('A idade é MAIOR que 17')


"""
if-elif-else

elif seria um else if do js
"""

linguagem = "Python"

if linguagem == "Swift":
    print('Swift')
elif linguagem == "Python":
    print("Python")
elif linguagem == "Angular":
    print("Angular")
else:
    print('Não é nenhuma das duas opções')


#Ternário
velocidade = 61

result = 'Multa' if velocidade > 60 else 'Não multado'
print(result)

#Estruturas de repetição com estruturas condicionais

for num in range(1,10):
    if num % 2 == 0:
        print('numero par', num)
    else:
        print('numero impar', num)