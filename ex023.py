"""num = input('Digite um numero: ')
n = str(num)
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(n [3]))
print('Dezena: {}'.format(n [2]))
print('Centena: {}'.format(n [1]))
print('Milhar: {}'.format(n [0]))"""

#Existe o jeito matematico de fazer porque se fizesse no primero so com 3 numeros ele quebra e nos ainda nao aprendemos condicoes e estruturas de repeticao
num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
