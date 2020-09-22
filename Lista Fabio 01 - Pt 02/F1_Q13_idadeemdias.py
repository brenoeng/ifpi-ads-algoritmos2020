# Entrada
anos = int(input('Digite sua idade em anos: '))
meses = int(input('Digite há quantos meses você fez aniversário: '))
dias = int(input('Digite quantos dias passou da sua data de aniversário: '))

# Processamento
idade_em_dias = anos * 365 + meses * 30 + dias

# Saída
print('Você tem {} dias de idade'.format(idade_em_dias))