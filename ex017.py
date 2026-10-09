from math import hypot
cateto_a = float(input('Digite um numero: '))
cateto_b = float(input('Digite outro numero: '))
hipotenusa = hypot(cateto_a, cateto_b)

print ('A hipotenusa deste triangulo e igual a {}'.format(hipotenusa))