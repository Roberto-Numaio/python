produtos = (
    'Arroz', 50.00,
    'Leite', 30.00,
    'Pao', 15.00,
    'Ovos', 25.00,
    'Acucar', 40.00,
    'Farinha', 20.00,
    'Manteiga', 60.00,
    'Queijo', 80.00,
    'Cafe', 45.00,
    'Frango', 120.00
)

print('-=-'*20)
print(f'{"Listagem de precos":^60}')
print('-=-'*20)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
