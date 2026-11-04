palavras = ('casa', 'computador', 'escola', 'python', 'livro', 'janela', 'flor', 'cadeira', 'programacao', 'estudante')

print('-=-'*20)
print(f'{"ANALISADOR DE VOGAIS":^60}')
print('-=-'*20)

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')