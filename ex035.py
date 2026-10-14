print('-=-'*20)
print('Escreva o comprimento/segmentos de 3 rectas diferentes para ver se forma um triangulo ou nao')
print('-=-'*20)
r1 = float(input('Digite o comprimento da recta 1: '))
r2 = float(input('Digite o comprimento da recta 2: '))
r3 = float(input('Digite o comprimento da recta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo')
else: 
    print('Os segmentos acima nao podem formar um triangulo')
