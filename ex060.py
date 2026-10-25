from time import sleep
print('-=-'*10)
print('Calculadora de fatorial')
print('-=-'*10)

num = int(input('Digite um numero para calcular o seu fatorial: '))
c = num
f = 1
print('Calculando fatorial de {}'.format(num))
sleep(1)
while c > 0: 
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))