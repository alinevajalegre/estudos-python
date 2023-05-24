import random

n1 = 'Luke'
n2 = 'Calum'
n3 = 'Ashton'
n4 = 'Michael'
lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)
print(escolhido)


random.shuffle(lista)
print(lista)