print('-=-'*10)
print('Soma de todos os numeros impares multiplos de 3 entre 1 e 500')
print('-=-'*10)
soma = 0
cont = 0
for c in range (1, 501, 2):  # Itera apenas sobre os números ímpares
    if c % 3 == 0:
        print(c, end=' ')
        soma += c
        cont += 1
print('\nA soma de todos os {} valores solicitados e: {}'.format(cont, soma))
