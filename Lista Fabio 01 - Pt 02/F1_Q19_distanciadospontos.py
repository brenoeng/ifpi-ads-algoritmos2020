# Entrada
xp1 = float(input('Digite o x do ponto 1: '))
yp1 = float(input('Digite o y do ponto 1: '))
xp2 = float(input('Digite o x do ponto 2: '))
yp2 = float(input('Digite o y do ponto 2: '))

# Processamento
d = ((xp2 - xp1) ** 2 + (yp2 - yp1) ** 2) ** 0.5

# Saída
print('A distância entre os pontos é {}'.format(d))