a = int(input('Digite o primiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#Verificando quem e menor
menor = a 
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print ('O menor numero entre {}, {} e {} e {}'.format(a,b,c,menor))
print ('O maior numero entre {}, {} e {} e {}'.format(a,b,c,maior))
