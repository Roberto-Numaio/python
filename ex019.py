from random import choice
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O aluno selecionado para limpar o quadro e: {}'.format(escolhido))
