"""
Ecrire l'algorithme de la suite de fibonacci:

C'est une suite définie par Un = Un-1 + Un-2

Si vous trouvez ça trop facile, passez par une fonction récursive
( c'est à dire fonction qui s'appelle elle meme)
"""

from fonctions_tools import inputIntPositif


def suite_fib_reach (limite:int)->list:
    '''
    suite_fib_reach => fonction fibo en renseignant la limite max
    '''
    suite_fib= [0,1]
    while suite_fib[-1] < limite:
        suite_fib.append(suite_fib[-1]+suite_fib[-2])
    return suite_fib



def suite_fib_nb (nombre:int)->list:
    '''
    suite_fib_nb => fonction fibo en renseignant le nb d'éléments
    '''
    suite_fib= [0,1]
    while nombre>0:
        suite_fib.append(suite_fib[-1]+suite_fib[-2])
        nombre-=1
    return suite_fib


print(suite_fib_reach(inputIntPositif("Jusqu'où voulez-vous voir la suite de Fibonacci? : ")))

print(suite_fib_nb(inputIntPositif("Combien d'éléments de la suite \
    de Fibonacci voulez-vous voir? : ")))
    