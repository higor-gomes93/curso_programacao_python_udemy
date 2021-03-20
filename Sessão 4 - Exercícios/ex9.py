'''
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é:
K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
'''

temp_celsius = float(input("Insira a temperatura em graus Celsius: "))
temp_kelvin = temp_celsius + 273.15
print(f"A temperatura em graus Kelvin eh {temp_kelvin}")