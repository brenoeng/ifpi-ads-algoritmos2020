# ENTRADA
num1 = int(input('Digite o valor do 1º numerador: '))
den1 = int(input('Digite o valor do 1º denominador: '))
num2 = int(input('Digite o valor para o 2º numerador: '))
den2 = int(input('Digite o valor para o 2º denominador: '))

# PROCESSAMENTO
mmc = den1 * den2
soma_numerador = int((mmc / den1) * num1 + (mmc / den2) * num2)

# Saída
print('A soma das frações é: {}/{}'.format(soma_numerador, mmc))