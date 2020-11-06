'''Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.'''
vetor = input('Insira os dados separados por virgula: ')
lista = vetor.split(',')

def repetido(lista):
    for i in lista:
        if lista.count(i) > 1:
            return True
        else:
            return False

if repetido(lista):
    print('Existem elementos repetidos')
else:
    print('Os elementos são unicos')