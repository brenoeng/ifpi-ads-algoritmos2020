# Exercicio 3.2 Item 5

def do_twice(f, valor):
    f(valor)
    f(valor)

def print_twice(palavra):
    print(palavra)
    print(palavra)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)
    
do_four(print, 'spam')