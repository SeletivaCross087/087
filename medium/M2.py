num = int(input('Digite o numero: '))
if num % 3 == 0 and num % 5 == 0:
    print('CrossBots')
elif num % 3 == 0:
    print('Cross')
elif num % 5 == 0:
    print('Bots')
else:
    print(num)