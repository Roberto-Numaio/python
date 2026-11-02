print('-=-'*10)
print('Analise de dados v.2.0')
print('-=-'*10)

total18 = totalH = totalM = 0
while True:
    print('-=-'*20)
    print('CADASTRE UMA PESSOA')
    print('-=-'*20)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo in 'M':
        totalH += 1
    if sexo in 'F' and idade < 20:
        totalM += 1
        resp = ' '
        while resp not in 'SN':
            print('-=-'*20)
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'Nn':
            break
print('Total de pessoas com mais de 18 anos: {}'.format(total18))
print('Ao todo temos {} homens cadastrados.'.format(totalH))
print('Sao ao todo {} mulheres menores de 20 anos.'.format(totalM))
