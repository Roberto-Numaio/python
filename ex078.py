lista = []
cont = 0

for l in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posicao {l}: ')))

print('-=-' * 20)
print(f'Voce digitou os valores {lista}')

maior = max(lista)

for v in lista:
    if v == maior:
        cont += 1

if cont == 1:
    print(f'O maior valor digitado foi {maior} na posicao', end=' ')
else:
    print(f'O maior valor digitado foi {maior} nas posicoes', end=' ')

for p, v in enumerate(lista):
    if v == maior:
        print(f'{p}...', end='')

print()

menor = min(lista)
cont = 0

for v in lista:
    if v == menor:
        cont += 1

if cont == 1:
    print(f'O menor valor digitado foi {menor} na posicao', end=' ')
else:
    print(f'O menor valor digitado foi {menor} nas posicoes', end=' ')

for p, v in enumerate(lista):
    if v == menor:
        print(f'{p}...', end='')
