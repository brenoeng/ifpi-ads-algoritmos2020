# Exercicio 3.2 Itens 2, 3 e 4

def do_twice(f, valor):
    f(valor)
    f(valor)

# def print_spam():
#     print('spam')

def print_twice(palavra):
    print(palavra)
    print(palavra)
    
do_twice(print_twice, 'spam')