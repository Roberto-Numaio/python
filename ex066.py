print('-=-'*20)
print('Contador de numeros')
print('-=-'*20)

cont = soma = 0
while True:
    num = int(input('Digite um numero [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Voce digitou {cont} numeros e a soma entre eles foi {soma}')
