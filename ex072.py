numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if  0 <= num <= 20:
        print(f'Voce digitou o numero {numeros[num]}')
    else:
        print('Numero invalido. Tente novamente.', end=' ')
