# Entrada
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))

# Processamento
horas_em_minutos = horas*60 + minutos

# Saída
print('{} horas e {} minutos equivalem a {} minutos'.format(horas, minutos, horas_em_minutos))