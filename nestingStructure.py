# https://www.codewars.com/kata/520446778469526ec0000001/train/python
# same_structure_as([1,[1,1]],[2,[2,2]]), True
# same_structure_as([1,[1,1]],[[2,2],2]), False

def same_structure_as(original, other):
    if type(original) is list and type(other) is list: # checagem simples e minimalista, fazendo uma varredura por tipo
        if len(original) == len(other): # checagem de length
            for i in range(0, len(original)):
                if same_structure_as(original[i], other[i]) != True: #checagem de valores
                    return False
        else:
            return False
    elif type(original) is list or type(other) is list: # checagem de tipo novamente, agora abordando o cenário caso não seja uma lista
        return False
    else:
        return True
    return True