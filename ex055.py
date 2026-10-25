print('-=-'*10)
print('Maior e menor pesos lidos')
print('-=-'*10)

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor peso lido foi {}Kg'.format(menor))