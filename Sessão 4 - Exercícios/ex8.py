'''
Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A fórmula de conversão é:
C = K - 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
'''

temp_kelvin = float(input("Insira a temperatura em graus Kelvin: "))
temp_celsius = temp_kelvin - 273.15
print(f"A temperatura em graus Celsius eh {temp_celsius}")