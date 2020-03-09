# Entrada
anos_fumando = int(input('Digite a quantidade de anos fumando: '))
cigarros_dia = int(input('Digite o número de cigarros por dia: '))
preco_carteira = int(input('Digite o preço da carteira de cigarro: '))

# Processamento
gasto = ((anos_fumando * 365 * cigarros_dia) / 20) * preco_carteira

# Saída
print('O gasto desse fumante é de R$ {}'.format(gasto))