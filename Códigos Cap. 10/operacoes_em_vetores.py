def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Mostrar Lista'
    menu += '\n 4 - Remover do Final'
    menu += '\n 5 - Remover do Início'
    menu += '\n 6 - Remover de Posição Específica'
    menu += '\n 7 - Inserir em Posição Específica'
    menu += '\n 8 - Média dos valores'
    menu += '\n N - <Crie diversas opções com os dados> '
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá parar em caso de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            # Listas quando passadas como argumentos e modificadas por
            # funções não é necessário retorná-las
            # Se modificar a lista dentro de um função, as variáveis que já
            # apontavam para ela, terão acesso a lista moficiada normalmente
            # Por isso nao está ```lista = inserir_valores(lista)````
            inserir_valores(lista)
        elif opcao == 2:
            mostrar_valor(lista)
        elif opcao == 3:
            mostrar_lista(lista)
        elif opcao == 4:
            remover_final(lista)
        elif opcao == 5:
            remover_inicio(lista)
        elif opcao == 6:
            remover_valor(lista)
        elif opcao == 7:
            inserir_valor_posicao(lista)
        elif opcao == 8:
            calcular_media(lista)
        elif opcao == 0:  # sair do while
            break
        else:
            print('Opção Inválida')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir? '))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')


def mostrar_valor(lista):
    posicao = int(input('Qual posição? '))
    if posicao < 0 or posicao > (len(lista)-1):
        print('Posição não existe')
    else:
        print('Valor buscado: ')
        print(lista[posicao])

    input('<enter> to continue...')

def mostrar_lista(lista):
    print("Sua lista: ", lista)
    input('\n<enter> to continue...\n')

def remover_final(lista):
    print(f"O valor '{lista.pop()}' foi removido da lista")
    input('\n<enter> to continue...\n')

def remover_inicio(lista):
    print(f"O valor '{lista.pop(0)}' foi removido da lista")
    input('\n<enter> to continue...\n')

def remover_valor(lista):
    posicao = int(input('Qual posição? '))
    print(f"O valor '{lista.pop(posicao)}' foi removido da lista")
    input('\n<enter> to continue...\n')

def inserir_valor_posicao(lista):
    valor = int(input('Valor: '))
    posicao = int(input('Posição: '))
    lista.insert(posicao, valor)
    print(f"O valor '{valor}' foi inserido")
    input('\n<enter> to continue...\n')

def calcular_media(lista):
    print("A média dos valores é: ", sum(lista)/len(lista))

main()