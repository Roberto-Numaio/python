from random import randint
from time import sleep #importa um temporizador que espera ate esse tempo acabar para seguir para a proxima accao
pc = randint(0, 5)
print('-=-' * 10)
print('Vou pensar num numero entre 0 e 5. Tente adivinhar!')
print('-=-' * 10)
user = int(input("Em que numero eu pensei: "))
print('PROCESSANDO...')
sleep(3) #cria um delay em segundos
if pc == user:
    print('PARABENS, voce ganhou!!!')
else: 
    print('GANHEI! Eu pensei no numero {} e nao {}'.format(pc, user))