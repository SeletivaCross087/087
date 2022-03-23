import math
x1 = int(input("Digite o x da primeira coordenada: "))
y1 = int(input("Digite o y da primeira coordenada: "))
x2 = int(input("Digite o x da segunda coordenada: "))
y2 = int(input("Digite o y da segunda coordenada: "))
x = x2 - x1
y = y2 - y1
dt = math.sqrt((x**2) + (y**2))
print(f'Distancia: {dt:.2f}')