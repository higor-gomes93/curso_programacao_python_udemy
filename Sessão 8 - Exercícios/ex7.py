'''
Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida em graus Fahrenheit. A fórmula
de conversão é: F = C*(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
'''

def temp_converter(celsius):
    fahrenheit = celsius*(9/5) + 32
    return round(fahrenheit, 2)

print(temp_converter(37))
print(temp_converter(12))
