lista = list()
impares = list()
pares = list()

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-=-'*30)
print(f'A lista completa e: {sorted(lista)}')
print(f'A lista de pares e: {pares}')
print(f'A lista de impares e: {impares}')
