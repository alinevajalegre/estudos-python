idade = int(input("Qual a idade? "))


if idade <= 9:
    categoria = 'mirim'
elif idade > 9 and idade <= 14:
    categoria = 'infantil'
elif idade > 14 and idade <= 19:
    categoria = 'junior'
elif idade > 19 and idade <=20:
    categoria = 'senior'
else:
    categoria = 'master'


print(categoria)