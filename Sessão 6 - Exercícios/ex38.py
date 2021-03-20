'''
Faça um programa que calcule o terno pitagórico a, b, c, para o qual a + b + c = 1000.
'''
valor = 1000

for a in range(1, 1000):
    for b in range(1, 1000):
        for c in range(1, 1000):
            var_a = a
            var_b = b
            var_c = c
            conta_1 = var_c + var_a + var_b
            conta_2 = (var_c**2) - (var_a**2) - (var_b**2)
            if conta_1 == valor and conta_2 == 0:
                print(f"As variáveis a, b e c são, respectivamente, {var_a}, {var_b} e {var_c}.")
                break
        if conta_1 == valor:
            break
    if conta_1 == valor:
        break  
        