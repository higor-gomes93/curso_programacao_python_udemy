'''
Faça uma função que receba 3 números inteiros como parâmetro, representando horas, minutos e segundos, e os converta
em segundos.
'''

def second(hour, minute, second):
    sec_h = hour*3600
    sec_m = minute*60
    sec_s = second
    total = sec_h + sec_m + sec_s
    return f'{total} segundos'

print(second(2, 30, 45))
