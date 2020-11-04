import os
import json

def main():
    celulares = inicializar('celulares.db')

    menu = tela_principal()
    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            celular = novo_celular()

            celulares.append(celular)
            print('Celular cadastrado com sucesso!')

        elif opcao == 2:
            mostrar_celulares(celulares)
        elif opcao == 3:
            buscar_celular(celulares)
        
        input('<enter> to continue...')
        opcao = int(input(menu))
    
    finalizar('celulares.db', celulares)

def tela_principal():
    menu = '***** App Jobs Cell ***** \n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Pesquisar celular\n'
    menu += '0 - Sair \n'
    menu += '\nopcao >>> '
    return menu

def inicializar(nome_arquivo):
    celulares_carregados = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        celulares_carregados = json.loads(dados)

    return celulares_carregados

def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()


def novo_celular():
    print('Criando novo celular')
    nome = input('Nome: ')
    marca = input('Marca: ')
    tela = input('Tela("): ')
    valor = float(input('Valor (R$): '))
    cam_frontal = input('Camera frontal (sim/não): ')
    
    celular = {}
    celular['nome'] = nome
    celular['marca'] = marca
    celular['tela'] = tela
    celular['valor'] = valor
    celular['cam_frontal'] = cam_frontal
    return celular

def mostrar_celulares(celulares):
    qtd = len(celulares)
    print(f'Listando {qtd} celulares')

    for celular in celulares:
        print('Nome: ', celular['nome'])
        print('Marca: ', celular['marca'])
        print('Valor: ', celular['valor'])
        print(12*'---')

def buscar_celular(celulares):
    nome_ou_marca = input('Digite o nome ou marca: ')
    print(nome_ou_marca)
    for celular in celulares:
        print(celular['nome'])
        if nome_ou_marca in (celular['nome'] or celular['marca']):
            print('ok')


main()