# Entrada
valor_dias = int(input('Informe o número de dias: '))

# Processamento
semanas = valor_dias // 7
dias = valor_dias % 7

# Saída
print('{} dias equivalem a {} semanas e {} dias'.format(valor_dias, semanas, dias))