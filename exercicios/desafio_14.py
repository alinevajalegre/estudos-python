celsius = float(input('Qual é a temp em celsius? '))

fahrenheit = (1.8*celsius) + 32
kelvin = celsius + 273

print('{} graus celsius em fahrenheit são: {:.2f} e em kelvin são {:.2f}'.format(celsius,fahrenheit, kelvin))