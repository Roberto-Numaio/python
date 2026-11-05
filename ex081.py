lista = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-=-'*30)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
print(f'O valor 5 faz parte da lista.' if 5 in lista else f'O valor 5 não foi encontrado na lista.')