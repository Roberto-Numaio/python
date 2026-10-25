from random import randint
from time import sleep 
print('-=-' * 10)
print('Vou pensar num numero entre 0 e 5. Tente adivinhar!')
print('-=-' * 10)
resposta = 'S'
palpites = 0
while resposta not in "Nn":
    pc = randint(0, 1)
    user = int(input("Em que numero eu pensei: "))
    print('PROCESSANDO...')
    sleep(1)
    if user == pc:
        resposta = "N"
        print('Voce acertou!!!')
    else:
        print('Voce errou, o pc pensou em {} e voce escolheu {}'.format(pc, user))
    resposta = input('Deseja jogar novamente [S/N]: ')
    palpites += 1
print('Foram necessarios {} palpites para acertar'.format(palpites))