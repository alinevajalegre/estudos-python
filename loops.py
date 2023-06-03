nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)


for x in "banana":
  print(x)

print("="*10)

nomes = ['Pedro', 'João', 'Leticia']
for n in nomes:
     print(n)
else:
     print("Todos os nomes foram listados com sucesso")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(2, 6):
  print(x)

"""
for loops cannot be empty, but if you for some reason have a for loop with no content, 
put in the pass statement to avoid getting an error.
"""
for x in [0, 1, 2]:
  pass