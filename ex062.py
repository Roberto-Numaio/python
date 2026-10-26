print('-=-'*10)
print('Progressao aritmetica v.3.0')
print('-=-'*10)
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('ACABOU')
    mais = int(input('\n Quantos termos voce quer mostrar a mais? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))
