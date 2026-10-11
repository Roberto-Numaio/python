salario = int(input('Digite o seu salario: '))
if salario >= 1250:
    print('PARABENS, voce recebeu um aumento de 10%. \n Seu salario antigo {}, O seu novo salario {}$'.format(salario,(salario*10)/100 + salario))
else:
    print('Parabens, voce recebeu um aumento de 15%. \n Seu salario antigo {}, O seu novo salario e {}$.'.format(salario,(salario*15)/100 + salario))
