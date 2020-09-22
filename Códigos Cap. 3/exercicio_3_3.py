<<<<<<< HEAD
# Exercicio 3.1 cap 3
def desenha_grade(colunas):
    grade_superiorinferior(colunas)
    do_four(print, ' ' * 8 + ('|' + ' ' * 9) * (colunas + 1))
    
def grade_superiorinferior(colunas):
    print(' ' * 8 + ('+ ' + '- ' * 4) * colunas + '+')

def do_twice(f, valor):
    f(valor)
    f(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)

colunas = 4
do_four(desenha_grade, colunas)
grade_superiorinferior(colunas)
# desenha_grade(4)
# desenha_grade(4)
# desenha_grade(4)
=======
# Exercicio 3.1 cap 3
def desenha_grade(colunas):
    grade_superiorinferior(colunas)
    do_four(print, ' ' * 8 + ('|' + ' ' * 9) * (colunas + 1))
    
def grade_superiorinferior(colunas):
    print(' ' * 8 + ('+ ' + '- ' * 4) * colunas + '+')

def do_twice(f, valor):
    f(valor)
    f(valor)

def do_four(f, valor):
    do_twice(f, valor)
    do_twice(f, valor)

colunas = 4
do_four(desenha_grade, colunas)
grade_superiorinferior(colunas)
# desenha_grade(4)
# desenha_grade(4)
# desenha_grade(4)
>>>>>>> 2da8176096b8ef3f9c6e6145859150771514812e
# desenha_grade(4)