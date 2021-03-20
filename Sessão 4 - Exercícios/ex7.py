'''
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A fórmula de conversão é:
C = 5*(F-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
'''

temp_fahrenheit = float(input("Insira a temperatura em graus Fahrenheit: "))
temp_celsius = 5*(temp_fahrenheit - 32.0)/9.0
print(f"A temperatura em graus Celsius eh {temp_celsius}")