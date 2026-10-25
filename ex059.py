n1 = int(input('Digite um numero: '))
n2 = int(input("digite outro: "))

opcao = 0
while opcao != 5:   
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    ''')
    opcao = int(input('Qual e a sua opcao? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O produto de {} x {} = {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else: 
            maior = 'nenhum, ambos sao iguais'
        print('O maior numero entre {} e {} e {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Digite um numero: '))
        n2 = int(input("digite outro: "))
    else:
        print('Opcao invalida! Tente novamente.')
    print('=-='*10, end='')
print('Fim do programa!')