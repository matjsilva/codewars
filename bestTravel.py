# choose_best_sum(230, 4, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]), 230
# choose_best_sum(430, 5, [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]), 430

# ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# t = limit
# k = number of towns

# ls split em k partes -> achar n <= t -> return n

import itertools

def choose_best_sum(t, k, ls):
    splits = list(itertools.combinations(ls, k))
    sums = [sum(i) for i in splits]
    finalSums = [i for i in sums if i <= t]
    if finalSums == []:
        resultado = None
    else:
        resultado = max([i for i in sums if i <= t])
    return resultado


    

