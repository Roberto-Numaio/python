total = totalmil = menor = cont = 0
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1:
        menor = preco
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('{:^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi de R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1000.00'.format(totalmil))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(produto, menor))
