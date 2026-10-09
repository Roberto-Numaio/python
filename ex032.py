ano = int(input('Digite um ano: '))
if (ano%400 == 0) or (ano%4 == 0):
    print('Ano bissexto')
else:
    print('Ano nao biseexto')