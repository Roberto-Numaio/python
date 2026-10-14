dista = float(input('Qual e a distancia da viagem: '))
if dista <= 200:
    print('O preco de passagem da viagem custa {:.2f} reais.'.format(dista*0.50))
else:
    print('O preco da passage da viagem custa {:.2f}reais.'.format(dista*0.45))
