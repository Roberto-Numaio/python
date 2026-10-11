from datetime import date 
print('-=-'*20)
print('PROGRAMA DE ALISTAMENTO MILITAR NACIONAL')
print('-=-'*20)
idade = int(input('em que ano voce nasceu? '))
ano = idade - date.today().year
if idade < 18:
    anos = 18 - ano
    print('Voce ainda nao tem idade suficiente para se alistar. Faltam {} anos para voce poder se alistar'.format(anos))
elif idade >= 18 and idade <= 35:
    print('Voce ja tem idade suficiente para se alistar.')
else:
    print('O tempo para voce se alistar ja se passou!')
