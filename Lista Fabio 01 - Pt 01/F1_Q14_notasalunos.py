# Entrada
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
peso1 = float(input('Peso 1: '))
peso2 = float(input('Peso 2: '))
peso3 = float(input('Peso 3: '))

# Processamento
media = (nota1*peso1 + nota2*peso2 + nota3*peso3) / (peso1 + peso2 + peso3)

# Saída
print('A média das notas é {}'.format(media))