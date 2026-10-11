n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro: '))

if n1 > n2:
    maior = n1
    print('O numero maior e {}'.format(maior))
elif n2 > n1:
    maior = n2
    print('O numero maior e {}'.format(maior))
else:
    print('Nao existe numero maior nem menor, os dois sao iguais!')
