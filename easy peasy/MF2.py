hr = int(input('Horas: '))
mes = hr//730
sem = hr//168
min = hr*60
seg = hr*3600
mil = hr*3600000
print(f'{hr} horas são:\n{mes} meses\n{sem} semanas\n{min} minutos\n{seg} segundos\n{mil} milisegundos')