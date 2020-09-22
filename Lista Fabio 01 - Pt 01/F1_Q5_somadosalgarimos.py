# Entrada
numero = int(input('Digite um número de 3 dígitos: '))

# Processamento
unidade = numero % 10
dezena = (numero // 10) % 10
centena = (numero // 10) // 10
soma = unidade + centena + dezena

# Saída
print('A soma dos algarismos do número {} é {} '.format(numero, soma))