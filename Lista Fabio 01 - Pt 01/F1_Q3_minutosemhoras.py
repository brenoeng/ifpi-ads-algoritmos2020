# Entrada
minutos_entrada = int(input('Minutos: '))

# Processamento
horas = minutos_entrada//60
minutos_saida = minutos_entrada%60

# Saída
print('{} minutos equivalem a {} horas e {} minutos'.format(minutos_entrada, horas, minutos_saida))