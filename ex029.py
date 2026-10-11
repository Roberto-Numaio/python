velocidade = int(input("Qual e a velocidade do carro em analise: "))
multa = 7 * (velocidade - 80)
if velocidade > 80:
    print('Excesso de velocidade!!!! \n Multado')
    print('A multa sera de {} reais'.format(multa))
else: 
    print('Obrigado por respeitar as normas da estrada')
print('Boa viagem.')