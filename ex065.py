print('-=-'*20)
print('Analise de dados (maior, menor e media dos valores fornecidos)')
print('-=-'*20)

res = "S"
cont = soma = media = maior = menor = 0
while res not in "Nn":
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    res = str(input('Quer continuar? [S/N] ')).strip()
print('Voce digitou {} numeros e a media entre eles foi {}'.format(cont, media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior, menor))
