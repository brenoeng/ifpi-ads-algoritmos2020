# Exercicio 3.1 cap 3

def right_justify(s):
    coluna70 = (70 - len(s))*" " + s
    print(coluna70)

right_justify('oi')