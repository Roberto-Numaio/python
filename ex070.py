print('-=-'*20)
print('LOJA SUPER BARATÃO')
print('-=-'*20)

total = totalmil = menor = cont = 0
prodBarato = " "
while True:
    produto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totalmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
            prodBarato = produto
    res = ' '
    while res not in 'SN':
        print('~'*30)
        res = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        print('~'*30)
    if res == 'N':
        break
print('{:^40}'.format('FIM DO PROGRAMA'))
print('O total da compra foi de R$ {:.2f}'.format(total))
print('Temos {} produtos custando mais de R$ 1000.00'.format(totalmil))
print('O produto mais barato foi {} que custa R$ {:.2f}'.format(prodBarato, menor))
