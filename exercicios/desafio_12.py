price = float(input('Qual é o preco do produto? '))

discount = int(input('Qual é a porcentagem de desconto? '))

total = price - (price*(discount/100))

print('O total com desconto de {}% é {:.2f}'.format(discount, total))

