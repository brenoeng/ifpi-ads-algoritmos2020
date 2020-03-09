# Entrada
valor_saque = float(input('Digite o valor a ser sacado: '))

# Processamento
notas100 = valor_saque // 100
notas50 = (valor_saque % 100) // 50
notas20 = ((valor_saque % 100) - 50) // 20 
notas10 = ((valor_saque % 100) - 50 - 20) // 10 
notas5 = ((valor_saque % 100) - 50 - 20) % 10 // 5 
notas2 = ((valor_saque % 100) - 50 - 20) % 10 % 5 // 2
notas1 = ((valor_saque % 100) - 50 - 20) % 10 % 5 % 2 

# Saída
print('Você receberá: ')
print('{} notas de 100'.format(notas100))
print('{} notas de 50'.format(notas50))
print('{} notas de 20'.format(notas20))
print('{} notas de 10'.format(notas10))
print('{} notas de 5'.format(notas5))
print('{} notas de 2'.format(notas2))
print('{} notas de 1'.format(notas1))