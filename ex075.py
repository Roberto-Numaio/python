numeros = (
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: ')),
    int(input('Digite um numero: '))
)

print(f'Os valores digitados foram: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
print(f'O numero 3 apareceu pela primera vez na posicao {numeros.index(3) + 1}' if 3 in numeros else 'O numero 3 nao foi digitado')
print(f'\nOs valores pares digitados foram: ')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
