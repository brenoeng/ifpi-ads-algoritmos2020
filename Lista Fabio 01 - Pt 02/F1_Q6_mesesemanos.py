# Entrada
valor_meses = int(input('Informe a quantidade de meses: '))

# Processamento
meses = valor_meses % 12
anos = valor_meses // 12

# Saída
print('{} meses equivalem a {} ano(s) e {} mês(meses)'.format(valor_meses, anos, meses))