# Entrada
custo_carro_fabrica = float(input('Custo do carro para a fábrica: '))

# Processamento
custo_carro_consumidor = custo_carro_fabrica * 1.28 + custo_carro_fabrica * 1.45

# Saída
print('O custo do carro para o consumidor é de R$ {}'.format(custo_carro_consumidor))