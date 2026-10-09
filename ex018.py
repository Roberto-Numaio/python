from math import sin, cos, radians, tan
num = int(input('Digite um numero em graus: '))
#python exige que os numeros estejam em radianos e nao em graus, por isso importamos radians e devemos converter!
radian = radians(num)
seno = sin(radian)
cosseno = cos(radian)
tangente = tan(radian)
print('O seno, cosseno e tangente de {} graus e igual a \n {}; \n {}; \n {}. \n respectivamente.'.format(num, seno, cosseno, tangente))