from random import shuffle
a1 = input('Nome do primeiro aluno: ')
a2 = input('Nome do segundo aluno: ')
a3 = input('Nome do terceiro aluno: ')
a4 = input('Nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentacao dos trabalhos dos alunos sera: ')
print(lista)
