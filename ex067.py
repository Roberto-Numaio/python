print('-=-'*10)
print('Tabuada infinita')
print('-=-'*10)

cont = 1
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num < 0:
        break
    print('-'*30)
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    cont = 1
    print('-'*30)
print('PROMAGA ENCERRADO!')
