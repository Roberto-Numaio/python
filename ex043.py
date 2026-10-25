print('-=-'*20)
print('Calculo de IMC')
print('-=-'*20)
peso = float(input('Qual e o seu peso (kg): '))
altura = float(input('Qual e a sua altura (m): '))
imc = peso/(altura**2)
print('Seu IMC e: {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Morbida, CUIDADO!!!!')