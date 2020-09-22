# Entrada
numero = int(input('Digite um número de 4 algarismos: '))

# Processamento
digito0 = numero % 10
digito1 = (numero // 10) % 10
digito2 = ((numero // 10) // 10) % 10
digito3 = ((numero // 10) // 10) // 10
soma = digito0 + digito1 + digito2 + digito3 

# Saída
print('A soma dos algarismos do número é {}'.format(soma))