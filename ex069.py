print('-=-'*10)
print('Analise de dados v.2.0')
print('-=-'*10)

total18 = totalH = totalM = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M/F]: ')).strip()
    if idade >= 18:
        total18 += 1
    if sexo in 'Mm':
        totalH += 1
    if sexo in 'Ff' and idade < 20:
        totalM += 1
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip()
        if resp in 'Nn':
            break
print('Total de pessoas com mais de 18 anos: {}'.format(total18))
print('Ao todo temos {} homens cadastrados.',format(totalH))
print('Sao ao todo {} mulheres menores de 20 anos.'.format(totalM))
