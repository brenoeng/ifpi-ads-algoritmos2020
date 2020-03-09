# Entrada
valor_segundos = int(input('Informe a quantidade de segundos: '))

# Processamento
segundos = valor_segundos % 60
minutos = valor_segundos // 60 % 60
horas = valor_segundos // 60 // 60

# Saída
print('{} segundos equivalem a {} horas, {} minutos e {} segundos'.format(valor_segundos, horas, minutos, segundos))