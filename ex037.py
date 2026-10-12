num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases de conversao: 
[ 1 ] Converter para BINARIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Qual e a sua opcao: '))
if opcao == 1: 
    print('{} Convertido para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} Convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} Convertido para HEXADECIMAl e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcao invalida. Tente novamente')