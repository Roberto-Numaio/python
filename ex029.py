vel = int(input("Qual e a velocidade do carro em analise: "))
velocidade = (80 - vel)*(-1)
multa = 7 * velocidade
if vel > 80:
    print('Excesso de velocidade!!!! \n Multado')
    print('A multa sera de {} reais'.format(multa))
else: 
    print('Obrigado por respeitar as normas da estrada')
print('Boa viagem.')