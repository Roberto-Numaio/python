from datetime import date
actual = date.today().year
nasc = int(input('Seu ano de nascimento: '))
idade = actual - nasc

print('O atleta tem {}'.format(idade))
if idade <= 9:
    print('Classificacao: Mirim')
elif idade <= 14:
    print('Classificacao: Infantil')
elif idade <= 19:
    print("JUNIOR") 
elif idade <= 25:
    print('Classificacao: Senior')
else:
    print('Classificacao: Master')
