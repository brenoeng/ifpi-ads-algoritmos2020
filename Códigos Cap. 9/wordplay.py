def main():
    # se nao achar o arquivo
    # https://stackoverflow.com/questions/49143852/trouble-opening-files-in-python-with-vs-code
    # "python.terminal.executeInFileDir": true,

    menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras sem letras proibidas\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            palavras_com_mais_de_20_letras()
        elif opcao == 2:
            palavras_sem_letra_e()
            # TODO
        elif opcao == 3:
            palavras_sem_letras_proibidas()
            # TODO
        else:
            print('Opção Inválida!')

        input('continuar <enter> ...')
        opcao = int(input(menu))

    print('Fim wordplay....')


def palavras_com_mais_de_20_letras():
    print('>> Palavras com + de 20 letras \n')
    arquivo = open('words.txt')

    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)

    arquivo.close()


def palavras_sem_letra_e():
    print('>> Palavras sem letra "e" \n')
    arquivo = open('words.txt')
    total = 0
    palavras_sem_e = 0

    for linha in arquivo:
        palavra = linha.strip()
        total += 1
        if has_no_e(palavra):
            palavras_sem_e += 1
            print(palavra)

    perc = (palavras_sem_e / total) * 100
    print(f'Total de Palavras: {total}')
    print(f'Palavras sem "e": {palavras_sem_e}')
    print(f'Percentual {perc} %')
    arquivo.close()


def has_no_e(palavra):
    # return 'e' not in palavra
    for letra in palavra:
        if letra == 'e':
            return False

    return True

def palavras_sem_letras_proibidas():
    print('>> Palavras sem letras proibidas \n')
    
    letras_proibidas = input('Digite as letras proibidas (separadas por virgula): ')
    palavras_sem_letras_proibidas = 0
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if proibidas(palavra, letras_proibidas):
            palavras_sem_letras_proibidas += 1
            print(palavra)

    print(f'Palavras sem "{letras_proibidas}": {palavras_sem_letras_proibidas}')
    arquivo.close()



def proibidas(palavra, letras_proibidas):
    for letra in palavra:
        if letra in letras_proibidas:
            return False
    return True

main()