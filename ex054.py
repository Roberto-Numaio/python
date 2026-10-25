from datetime import date
actual = date.today().year
print('-=-'*10)
print('Verificacao de idade')
print('-=-'*10)

maior = 0
menor = 0
for c in range(1, 8):
    ano_nascimento = int(input('Em que ano nasceu a {}º pessoa: '.format(c)))
    idade = actual - ano_nascimento
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Há {} pessoas maiores de idade'.format(maior))
print('Há {} pessoas menores de idade'.format(menor))