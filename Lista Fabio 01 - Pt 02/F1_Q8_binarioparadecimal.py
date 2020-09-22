# Entrada
numero = int(input('Digite um número binário de 4 bits: '))

# Processamento
digito0 = numero % 10
digito1 = (numero // 10) % 10
digito2 = ((numero // 10) // 10) % 10
digito3 = ((numero // 10) // 10) // 10

decimal = digito3 * 2 ** 3 + digito2 * 2 ** 2 + digito1 * 2 ** 1 + digito0 * 2 ** 0

# Saída
print('O binário {} equivale a {} em decimal'.format(numero, decimal))