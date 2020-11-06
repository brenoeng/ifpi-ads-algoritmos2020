vetor = input('Insira o binario (8 bits) separando os algarismos por espaços: ')
lista = vetor.split()

def bin_dec(lista):
    # binario para decimal
    decimal = 0
    for i in range(len(lista)):
        decimal += ( int(lista[i]) * 2**(len(lista)-1-i) )
    return decimal

def converte_hexa(decimal):
    if decimal == 10:
        return 'A'
    elif decimal == 11:
        return 'B'
    elif decimal == 12:
        return 'C'
    elif decimal == 13:
        return 'D'
    elif decimal == 14:
        return 'E'
    elif decimal == 15:
        return 'F'
    else:
        return decimal

# binario para hexadecimal
algarismo_1 = converte_hexa(bin_dec(lista[0:4]))
algarismo_2 = converte_hexa(bin_dec(lista[4:]))
print(bin_dec(lista[0:4]))
hexadec = f'{algarismo_1}{algarismo_2}'

print(f'Decimal: {bin_dec(lista)}')
print(hexadec)