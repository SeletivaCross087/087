dc = int(input("Insira o valor em decimal: "))
bn = bin(dc)
lt = bn
tm = len(str(lt))
x = str(bn)
y = 0
for i in range(0, tm):
    if x[i] == '1':
        y = y + 1
print(f'Quantidade de 1: {y}\nBinario: {bn[3:]}\n')
