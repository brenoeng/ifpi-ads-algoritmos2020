# Entrada
velocidade_kmh = int(input('Velocidade km/h: '))

# Processamento
velocidade_ms = velocidade_kmh / 3.6

# Saída
print('{} km/h é igual a {} m/s'.format(velocidade_kmh, velocidade_ms))