# Entrada
valor_horas = int(input('Informe a quantidade de horas: '))

# Processamento
horas = valor_horas % 24
dias = valor_horas // 24 % 7
semanas = valor_horas // 24 // 7

# Saída
print('{} horas equivalem a {} semanas, {} dias e {} horas'.format(valor_horas, semanas, dias, horas))