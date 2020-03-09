# Entrada
dias = int(input('Digite sua idade em dias: '))

# Processamento
idade_em_dias = dias % 30
idade_em_meses = (dias // 30) % 12
idade_em_anos = (dias // 30) // 12

# Saída
print('Você tem {} anos, {} meses e {} dias de idade'.format(idade_em_anos, idade_em_meses, idade_em_dias))