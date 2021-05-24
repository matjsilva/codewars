# count_patterns_from('A',10), 0
# count_patterns_from('A',0),  0
# count_patterns_from('E',2),  8

# é bem simples, quantos padrões existem desde a letra firstPoint, com outros length caracteres?
# trata-se de uma combinação de letras, firstPoint -> (i in range(0, length))-1

# [A, B, C]
# [D, E, F]
# [G, H, I]

from itertools import combinations, permutations

def count_patterns_from(firstPoint, length):
    lst = "ABCDEFGHI"
    allp = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9
    }
    resultado = []

    # avançar gradualmente em uma matriz seguindo o id do dicionário allp

    if len(firstPoint) == 1 and firstPoint in lst:
        actual = allp[firstPoint]
        return actual

        # for j in allp:
        #     combPass = combinations(j, length)
        #     for i in combPass:
        #         try:
        #             if j.index(firstPoint) - j.index(i) == length-1 or j.index(firstPoint) - j.index(i) == (length-1)*-1:
        #                 resultado.append(i)
        #         except ValueError:
        #             pass
        
        # return len(resultado)
    # allp = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    # if len(firstPoint) == 1 and firstPoint in allp:
    #     if length != 2:
    #         combPoss = combinations(allp, length)
    #         return len([' -> '.join(i) for i in combPoss if firstPoint in i])
    #     else:
    #         combPoss = combinations(allp[firstPoint], length)
    #         return len([' -> '.join(i) for i in combPoss if firstPoint in i and allp.index(firstPoint)])


    # if len(firstPoint) == 1 and firstPoint in allP[j for j in allP]:
    #     for j in allP:
    #         print(j)
    #         for i in allP[j]:
    #             combPoss = combinations(allP[i], length)
    #             print(i)
    #             return len([' -> '.join(i) for i in combPoss if firstPoint in i])

    # if len(firstPoint) == 1 and firstPoint in all:
    #     combPoss = combinations(all, length)
    #     if length > 2:
    #         return len([' -> '.join(i) for i in combPoss if firstPoint in i])

print(count_patterns_from("A", 10))
print(count_patterns_from("A", 0))
print(count_patterns_from("E", 2))
print(count_patterns_from('C', 2))
print(count_patterns_from('E', 4))
