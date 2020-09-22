# Entrada
numero = int(input('Digite um número de 3 dígitos: '))

# Processamento
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 10) // 10
inverso = 100*unidade + 10*dezena + 1*centena

# Saída
print('O inverso do número {} é {} '.format(numero, inverso))