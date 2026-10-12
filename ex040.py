n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('Aluno aprovado com media {}'.format(media))
elif 7 > media >=5:
    print('Aluno em recuperacao media {}'.format(media))
elif n1 < 0 or n2 < 0:
    print('Valor invalido. Volte a inserir as notas') 
else:
    print('Aluno reprovado media {}'.format(media))
