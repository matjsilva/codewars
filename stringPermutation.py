# sorted(permutations('a')), ['a']
# sorted(permutations('ab')), ['ab', 'ba']

import itertools 

def permutations(string):
    resultado = [] # lista final
    sep = '' # separador string para poder usar a função join a fim de formar a permutação final
    possib = itertools.permutations(string) # utilizando o módulo itertools e sua função permutations
    for permut in possib: # para cada permutação...
        resultado.append(sep.join(permut)) # adicionar a permutação formada com o separador na lista final
    resultado = list(dict.fromkeys(resultado)) # eliminando duplicatas
    return resultado # fim :)

print(permutations('aabb'))