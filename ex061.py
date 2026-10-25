print('-=-'*10)
print('Progressao aritmetica v.2.0')
print('-=-'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} '.format(termo), end='')
    termo += razao
    cont += 1
print('ACABOU')