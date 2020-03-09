# Entrada
valor_minutos = int(input('Informe a quantidade de minutos: '))

# Processamento
minutos = valor_minutos % 60
horas = valor_minutos // 60 % 24
dias = valor_minutos // 60 // 24

# Saída
print('{} minutos equivalem a {} dia(s), {} hora(s) e {} minuto(s)'.format(valor_minutos, dias, horas, minutos))