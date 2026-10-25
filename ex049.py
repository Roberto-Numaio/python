print('-=-'*10)
print('Tabuada v2.0')
print('-=-'*10)
num = int(input('Digite um numero para ver sua tabuada: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(num, c, num*c))
