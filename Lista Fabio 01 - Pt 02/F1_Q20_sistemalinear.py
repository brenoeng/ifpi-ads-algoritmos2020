# Entrada
a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))
d = float(input('Digite o coeficiente d: '))
e = float(input('Digite o coeficiente e: '))
f = float(input('Digite o coeficiente f: '))

# Processamento
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# Saída
print('O valor de x é {} e y é {}'.format(x, y))