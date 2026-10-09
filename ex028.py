import random
pc = random.randint(1, 2)
user = int(input("Digite um numero: "))
print('=======Analisando=========')
if pc == user:
    print('Voce acertou')
else: 
    print('Tente novamente')