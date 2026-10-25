print('-=-'*10)
print('Analise de dados (sexo, idade e nome)')
print('-=-'*10)

soma = 0
mediaIdade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Digite o nome da {}º pessoa: '.format(p))).strip()
    idade = int(input('Digite a idade da {}º pessoa: '.format(p)))
    sexo = str(input('Digite o sexo da {}º pessoa [M/F]: '.format(p ))).strip()

    #soma e calcula a media de idade
    soma += idade
    mediaIdade = soma / 4

    #nome do homem mais velho
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    #mulheres maiores de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

print('A média de idade do grupo é de {} anos'.format(mediaIdade))
print('O homem mais velho é {} e ele tem {} anos'.format(nomevelho, maioridadehomem))
print('Existem {} mulheres com menos de 20 anos'.format(totmulher20))