print('='*10, end='')
print(' LOJA NUMAIO ', end='')
print('='*10)

preco = int(input('Valor a ser pago: '))

print('[ 1 ] Pagar a vista em dinheiro/cheque')
print('[ 2 ] Pagar a vista com cartao')
print('[ 3 ] Pagar em ate 2x no cartao')
print('[ 4 ] Pagar 3x ou mais no cartao')
opcao = int(input('Como vai proceder? '))

if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcela em 2x de {:.2f}$ sem juros'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas: '))
    if totalparc < 3:
        print('reinicie o programa e escolha a opcao correspondente a sua escolha')
    parcela = total / totalparc
    print('Sua compra sera parcela em {}x de {:.2f}$ com juros'.format(totalparc, parcela))
else:
    print('Opcao invalida!')
print('A sua compra de {:.2f} vai custar {:.2f} no final'.format(preco, total))