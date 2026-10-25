from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint (0, 2)
print('''Suas opcoes: 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('sua jogada sera: '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('-=-'*10)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-=-'*10)

if computador == 0: #Computador jogou pedra
    if jogador == 0: #jogador jogou pedra
        print('Empate')
    elif jogador == 1: #jogador jogou papel
        print('Jogador vence')
    elif jogador == 2: #jogador jogou tesoura
        print('Compuatdor vence')
elif computador == 1: #computador jogou papel
    if jogador == 0: #jogador jogou pedra
        print('compuatdor vence')
    elif jogador == 1: #jogador jogou papel
        print('Empate')
    elif jogador == 2: #jogador jogou tesoura
        print('Jogador vence')
elif computador == 2: #compuatdor jogou tesoura
    if jogador == 0: #jogador jogou pedra
        print('Jogador vence')
    elif jogador == 1: #jogador jogou papel
        print('Compuatdor vence')
    elif jogador == 2: #jogador jogou tesoura
        print('Empate')
