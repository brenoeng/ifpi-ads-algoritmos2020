# Entrada
valor_metros = int(input('Valor em metros: '))

# Processamento
km = valor_metros // 1000
m = valor_metros % 1000

# Saída
print('{} metros equivalem a {} quilômetros e {} metros'.format(valor_metros, km, m))