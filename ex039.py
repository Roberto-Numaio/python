from datetime import date 
print('-=-'*20)
print('PROGRAMA DE ALISTAMENTO MILITAR NACIONAL')
print('-=-'*20)
actual = date.today().year
nasc = int(input('em que ano voce nasceu? '))
idade = actual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, actual))
if idade == 18:
    print('Voce tem que se alistar imediatamente')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    ano = actual + saldo
    print('Seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado a {} anos!'.format(saldo))
    ano = actual - saldo
    print('Seu alistamento foi em {}'.format(ano))
