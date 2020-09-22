def main():
    print("")
    numeros = int(input('Quantos números você quer digitar? > '))
    lista_numeros = recebe_numeros(numeros)
    verifica_numeros(lista_numeros)
    lista_atualizada = dobro_positivo_metade_negativo(lista_numeros)
    verifica_numeros(lista_atualizada)
    print('A média dos valores da lista atualizada é: ', calcula_media(lista_atualizada))


def recebe_numeros(qtd_numeros):
    vetor_numeros = [-1]*qtd_numeros
    for i in range(qtd_numeros):
        vetor_numeros[i] = int(input(f'Digite o  {i+1}º número > '))
    return vetor_numeros

def dobro_positivo_metade_negativo(lista):
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = lista[i]/2
        else:
            lista[i] = lista[i]*2
    return lista
    
def verifica_numeros(lista):
    pares = 0
    impares = 0
    negativos = 0
    positivos = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            negativos += 1
        else:
            positivos += 1
                
        if lista[i]%2 == 0:
            pares += 1
        else:
            impares += 1

    print(f'Você digitou: {pares} números pares, {impares} números impares, {negativos} números negativos, {positivos} números positivos')

def calcula_media(lista):
    return sum(lista)/len(lista)

main()



