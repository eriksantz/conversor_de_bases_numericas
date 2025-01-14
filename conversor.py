num = int(input('Digite um número inteiro: '))
# conversão
binario = bin(num)[2:]
octal = oct(num)[2:]
hexa = hex(num)[2:]

print('Escolha uma das bases para conversão: ')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')

num1 = int(input('Sua opção: '))

if num1 == 1:
    print(f'Seu número convertido para BINÁRIO é igual a {binario}')
elif num1 == 2:
    print(f'Seu número convertido para OCTAL é igual a {octal}')
elif num1 == 3:
    print(f'Seu número convertido para HEXADECIMAL é igual a {hexa}')
else:
    print('Opção inválida! Escolha 1, 2 ou 3.')
