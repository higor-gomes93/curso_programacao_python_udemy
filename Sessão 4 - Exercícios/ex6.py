'''
Leia uma temperatura em graus Celsius e apresenta-a convertida em graus Fahrenheit. A fórmula de conversão é: 
F = C*(9.0/5.0)+32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
'''

temp_celsius = float(input("Insira a temperatura em graus Celsius: "))
temp_fahrenheit = (temp_celsius*(9.0/5.0))+32
print(f"A temperatura em graus Fahrenheit eh {temp_fahrenheit}")