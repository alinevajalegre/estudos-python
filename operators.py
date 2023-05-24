number_1 = 5
number_2 = 2

soma = number_1 + number_2
subtracao = number_1 - number_2
multiplicacao = number_1 * number_2
divisao = number_1 / number_2
divisao_inteira = number_1 // number_2
modulo = number_1 % number_2 #resto da divisao
exponenciacao = number_1 ** number_2

print(soma) # 7
print(subtracao) # 3
print(multiplicacao)  # 10
print(divisao) # 2.5
print(divisao_inteira) # 2
print(modulo)  # 1
print(exponenciacao) # 25


#OPERADORES DE ATRIBUICAO
print('#operadores de atribuicao#')
x = 2

x += 1  #x = x+1
x -= 1 # x = x-1
x *= 1 # x = x * 1
x /= 1 # x = x / 1
x %= 1 # x = x % 1

print(x)

#0PERADORES DE COMPARACAO

print('#operadores comparacao#')
b = 3
c = 2

print(b>c) #maior que
print(b<c) #menor que
print(b==c) #igual a
print(b!=c) #diferente de
print(b>=c) #maior ou igual
print(b<=c) #menor ou igual

#OPERADORES DE IDENTIDADE
#IS E IS NOT

time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")

#OPERADORES LOGICOS
#and or e not
idade_lucas = 21
idade_carolina = 19

# OPERADOR OR
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

# OPERADOR AND
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")


#OPERADORES DE ASSOCIACAO
#IN e NOT IN

frutas = ["banana","laranja","uva","ameixa"]

fruta_1 = "ameixa"
fruta_2 = "melancia"

print(fruta_1 in frutas) # True
print(fruta_2 in frutas) # False