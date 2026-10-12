casa = float(input('Qual e o valor da casa? '))
salario = int(input('Qual e o seu salario? '))
anos = float(input('Em quantos anos voce vai pagar? '))
parcela = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f}$ a prestacao sera de {:.2f}$'.format(casa, parcela))
if parcela <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo NEGADO')