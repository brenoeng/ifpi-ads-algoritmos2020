# Exercício 3.2 Item 1

def do_twice(f):
    f()
    f()

def print_spam():
    print('spam')
    
do_twice(print_spam)