print('-=-'*10)
print('Soma de numeros pares')
print('-=-'*10)

soma = 0
cont = 0
fim = int(input('Digite o valor final: '))
for c in range (1, fim+1): 
    num = int(input('Digite o {}º numero: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce me deu {} numeros, {} sao pares. A soma dos pares e: {}'.format(fim, cont,soma))