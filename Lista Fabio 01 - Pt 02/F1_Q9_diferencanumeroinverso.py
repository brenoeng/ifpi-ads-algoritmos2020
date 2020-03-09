# Entrada
numero = int(input('Digite um número de 3 dígitos: '))

# Processamento
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 10) // 10
inverso = unidade * 100 + dezena * 10 + centena
diferenca = numero - inverso

# Saída
print('A diferença do número {} e seu inverso é {} '.format(numero, diferenca))