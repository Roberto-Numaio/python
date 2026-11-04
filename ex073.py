equipa = (
    'Flamengo',
    'Palmeiras',
    'Cruzeiro',
    'Fluminense',
    'Athletico-PR',
    'Bahia',
    'Atlético-MG',
    'RB Bragantino',
    'Santos',
    'São Paulo',
    'Coritiba',
    'Mirassol',
    'Botafogo',
    'Vasco',
    'Vitória',
    'Internacional',
    'Grêmio',
    'Corinthians',
    'Remo',
    'Chapecoense'
)

print('-=-'*20)
print(f'{"CAMPEONATO BRASILEIRO 2026"}')
print('-=-'*20)

print(f'Os 5 primeiros colocados sao: {equipa[0:5]}')
print('-=-'*20)

print(f'Os 4 ultimos colocados sao: {equipa[-4:]}')
print('-=-'*20)

print(f'OS times em ordem alfabetica sao: {sorted(equipa)}')
print('-=-'*20)

print(f'O Chapecoense esta na {equipa.index("Chapecoense") + 1}ª posicao')
print('-=-'*20)
