'''
Calcule as raízes de uma equação de segundo grau.
'''
import math as m

# Coletando os parâmetros
print("Ola. Este programa calcula as raizes de uma equacao do tipo ax² + bx + c = 0.")
var_a = float(input("Insira o valor do parametro a: "))
var_b = float(input("Insira o valor do parametro b: "))
var_c = float(input("Insira o valor do parametro c: "))

# Calculando delta e x
delta = (var_b**2) - 4*var_a*var_c

# Resultados
if var_a != 0:
    if delta > 0:
        var_x1 = (-var_b + m.sqrt(delta))/(2*var_a)
        var_x2 = (-var_b - m.sqrt(delta))/(2*var_a)
        print(f"Existem duas raizes reais e seus valores sao {var_x1} e {var_x2}.")
    elif delta == 0:
        var_x = (-var_b)/(2*var_a)
        print(f"Existe uma unica raiz de valor {var_x}")
    else:
        print("Nao existe raiz real.")
else:
    print("Nao eh equacao de segundo grau.")

