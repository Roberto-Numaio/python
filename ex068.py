from random import randint
print('-=-'*10)
print('Jogo do Par ou Impar')
print('-=-'*10)

while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um numero (0 a 10): '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input('Par ou Impar? [P/I] ').strip().upper()[0]
        total = pc + jogador
    print(f'Voce jogou {jogador} e o computador {pc}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if escolha == 'P':
        if total % 2 == 0:
            print('-=-'*10)
            print('Voce VENCEU!')
            print('Vamos jogar novamente...')
            print('-=-'*10)
        else:
            print('Voce PERDEU!')
            break
    if escolha == 'I':
        if total % 2 == 1:
            print('-=-'*10)
            print('Voce VENCEU!')
            print('Vamos jogar novamente...')
            print('-=-'*10)
        else:
            print('Voce PERDEU!')
            break