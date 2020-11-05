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
    menu = '\n***** App Jobs Cell ***** \n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Pesquisar celular\n'
    menu += '0 - Sair \n'
    menu += '\nopcao >>> '
    return menu

def tela_detalhes(celular):
    nome = celular['nome']
    menu = f'+++++ Voce selecionou o celular {nome}. O que deseja fazer agora? +++++  \n'
    menu += '1 - Mostrar Detalhes\n'
    menu += '2 - Remover\n'
    menu += '3 - Editar\n'
    menu += '4 - Duplicar\n'
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
    
    nome_ou_marca = input('\nDigite o nome ou marca: ')
    # print(nome_ou_marca)
    contador = 0
    celulares_listados = []
    for celular in celulares:
        if celular['nome'].startswith(nome_ou_marca) or celular['marca'].startswith(nome_ou_marca):
            contador += 1
            print(f'\n>>>>> {contador} <<<<<')
            print('Nome: ', celular['nome'])
            print('Marca: ', celular['marca'])
            print('Valor: ', celular['valor'])
            print(12*'---')
            celulares_listados.append(celular)
        
    if contador == 0:
        print('Celular ou marca não encontrado nos registros!')
    else:
        entrar_no_submenu = input('Deseja selecionar um celular? (sim/nao) ')
        if entrar_no_submenu == 'sim' or entrar_no_submenu == 's':
            celular_escolhido = int(input('\nDigite o número do celular que deseja selecionar> '))
            sub_menu(celulares_listados, celulares, celular_escolhido)
        else:
            pass
    
    

def sub_menu(celulares_listados, celulares, celular_escolhido):
    print(celulares)
    menu = tela_detalhes(celulares_listados[celular_escolhido-1])
    opcao = int(input(menu))
    
    while opcao != 0:
        if opcao == 1:
            mostrar_detalhes(celulares_listados[celular_escolhido-1])
        elif opcao == 2:
            remover_celular(celulares_listados, celulares, celular_escolhido)
        elif opcao == 3:
            pass
        input('<enter> to continue...')
        opcao = int(input(menu))

    finalizar('celulares.db', celulares)

def mostrar_detalhes(celular):
    print('Nome: ', celular['nome'])
    print('Marca: ', celular['marca'])
    print('Valor: ', celular['valor'])
    print('Tela: ', celular['tela'])
    print('Camera frontal: ', celular['cam_frontal'])
    print(12*'---')

def remover_celular(celulares_listados, celulares, celular_escolhido):
    indice = -1
    for item in celulares:
        indice += 1
        if item['nome'] == celulares_listados[celular_escolhido-1]['nome']:
            celulares.pop(indice)

    print('Celular removido com sucesso!') 
    

main()