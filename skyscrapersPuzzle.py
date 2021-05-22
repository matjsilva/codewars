# clues = ( 3, 2, 2, 3, 2, 1,
#           1, 2, 3, 3, 2, 2,
#           5, 1, 2, 2, 4, 3,
#           3, 2, 1, 2, 2, 4)

# expected = (( 2, 1, 4, 3, 5, 6 ),
#             ( 1, 6, 3, 2, 4, 5 ),
#             ( 4, 3, 6, 5, 1, 2 ),
#             ( 6, 5, 2, 1, 3, 4 ),
#             ( 5, 4, 1, 6, 2, 3 ),
#             ( 3, 2, 5, 4, 6, 1 ))

# como funciona o puzzle:
# -----------------------
#               6 skyscrapers, cada um com uma altura (max: 6)
# 6 prédios visíveis da esquerda [][][][][][] 1 prédio visível da direita
# logo: 6 [1][2][3][4][5][6] 1

# isso porque na esquerda, 6 prédios são visíveis, logo, menor ao maior, todas as alturas precisam ser diferentes umas das outras, e prédios maiores bloqueiam menores, logo, um prédio de altura máxima na direita permite que apenas 1 prédio seja visto, o próprio prédio de 6 andares.

# as clues são quantos prédios é possível ver, formando o array multi-dimensional final em sentido horário, ou seja:

#     0  1  2  3  4  5 
# 23 [ ][ ][ ][ ][ ][ ] 6
# 22 [ ][ ][ ][ ][ ][ ] 7
# 21 [ ][ ][ ][ ][ ][ ] 8      assim, clues = (0, 1, 2, 3, 4, 5,
# 20 [ ][ ][ ][ ][ ][ ] 9                      6, 7, 8, 9, 10, 11,
# 19 [ ][ ][ ][ ][ ][ ] 10                    12, 13, 14, 15, 16, 17
# 18 [ ][ ][ ][ ][ ][ ] 11                    18, 19, 20, 21, 22, 23)
#    17 16 15 14 13 12 

# é fácil de entender com a visualização horizontal, levando em consideração que se trata de uma questão lógica básica, se 6 é visto da esquerda, o maior vai estar no final, pois todos são visíveis, apenas 1 vai ser visto na direita, uma 'escada' de prédios.
# agora, considerando a visualização vertical, fica um pouco mais complicado.
# entretando, eu tive uma ideia.

# em casos mais simples, 1 é apenas o maior valor em frente ao index do array corespondente, e 6 é o menor. o problema é quando é possível visualizar 1 de um lado e 2 de outro, seria 6 e 1 seguido do menor numero entre os maiores numeros.
# confuso.

# lendo algumas discussões sobre casos parecidos, descobri o método constraint satisfation, ou satisfação de restrição, o qual é usado em processos de inteligência artificial, esse é o método mais difícil de realizar, com maiores chances de conseguir um resultado correto, além de ter uma estrutura de código limpa, pra tornar isso possível, preciso criar um algoritmo de backtracking.
# é... vai ser dificil.

from itertools import permutations

# processos
# primeiro de tudo, como eu disse acima, lidar com uma direção por vez é mais fácil (quebrando o problema em partes pequenas, divisão e conquista)
#   tratar os dados do tuple clues | feito!
#   construir coluna, construir linha | (validar coluna, validar linha) | feito!
#   descobrir possibilidades (validar) | 
#   construir dict com possibilidades válidas
#   resolver!

# TRATAMENTO DE DADOS
def treatClue(clues, sideLen):
    top = clues[0:sideLen]              # simples, indo do início do array até o valor da lateral
    right = clues[sideLen:sideLen*2]    # mudando lado, multiplicando valores, isso porque, como eu expliquei anteriormente, a tuple clues é formada em sentido horário da matriz
    bottom = clues[sideLen*2:sideLen*3] 
    left = clues[sideLen*3:sideLen*4]

    return top, right, bottom, left

def visible(tList): # sinceramente, essa é a função mais interessante dentre as outras
    aTallestH = 0 # essa var é reservada para a maior altura da coluna/linha a ser checada pela função recursiva
    tVisibleC = 0 # essa é a contagem de prédios visíveis, que achei melhor não deixar como s de skyscraper, mas sim t de tower por motivos de repetição
    for tH in tList: # aqui, eu checo a altura do prédio na lista de prédios, dentro da sub-lista da matriz a ser checada, seja coluna ou linha
        if tH > aTallestH: # se a altura for maior que o maior prédio atual
            tVisibleC += 1 # a contagem de prédios visíveis ganha um novo membro!
            aTallestH = tH # assim, o maior prédio se torna este prédio, sério, essa função é muito linda.
    
    return tVisibleC

def visualPossib(gridSizeLen): # muito complicado pra explicar com palavras, mas em resumo, eu descubro os prédios visíveis, adiciono eles no grande array multi-dimensional, junto de uma variável em processo de iteração levando em consideração o tamanho do grid (incrementado). 
    return [*[(visible(reversed(i)), i) for i in permutations([i for i in range(1, gridSizeLen + 1)])],
            *[(0, visible(reversed(i)), i) for i in permutations([i for i in range(1 ,gridSizeLen + 1)])],
            *[(visible(i), 0, i) for i in permutations([i for i in range(1, gridSizeLen + 1)])],
            *[(0, 0, i) for i in permutations([i for i in range(1, gridSizeLen + 1)])]] 

def possibLines(tVisible, otherSideTVisible, visPosList):
    return list(map(lambda g: g[2], filter(lambda g: g[0] == tVisible and g[1] == otherSideTVisible, visPosList)))

def lineValid(line, gridSize): # ferramenta pra validar uma linha, útil, simples e objetivo
    return len(set(line)) == gridSize

def lineWBoundsPossib(line, l, r):
    return (l == 0 or visible(line) == l) and (r == 0 or visible(line) == r)

def splitDictRC(dictPossib, gridSize):
    possibXC = [makeColumns(i, dictPossib, gridSize) for i in range(gridSize)]
    possibXR = [makeRows(i, dictPossib, gridSize) for i in range(gridSize)]
    return validateLines(possibXR, gridSize), validateLines(possibXC, gridSize)

# CONSTRUÇÃO DE OBJETOS
def makeRowsRec(x, y, aPoss, gridSize): # função recursiva da build das linhas
    possibleVal = aPoss.get((x, y), [])
    if x >= gridSize:
        return [None]
    resultado = [[value] if j is None else [value, *j] for value in possibleVal for j in makeRowsRec(x=x+1, y=y, aPoss=aPoss, gridSize=gridSize)]
    return resultado

def makeRows(y, aPoss, gridSize): # build da linha
    return list(map(lambda i: i, filter(lambda i: i is not None and len(i) == gridSize, makeRowsRec(x=0, y=y, aPoss=aPoss, gridSize=gridSize))))

def makeColumnsRec(x, y, aPoss, gridSize): # função recursiva da builda das colunas
    possibleVal = aPoss.get((x, y), [])
    if y >= gridSize:
        return [None]
    resultado = [[value] if j is None else [value, *j] for value in possibleVal for j in makeRowsRec(x=x, y=y+1, aPoss=aPoss, gridSize=gridSize)]
    return resultado

def makeColumns(x, aPoss, gridSize): # builda da coluna
    return list(map(lambda i: i, filter(lambda i: i is not None and len(i) == gridSize, makeColumnsRec(x=x, y=0, aPoss=aPoss, gridSize=gridSize))))

def makeDictPossibRC(possibRList, possibCList, cells): # dict de valores possíveis
    return dict(((x,y), {possibC[y] for possibC in possibCList[x]} & {possibR[x] for possibR in possibRList[y]}) for x, y in cells) # devo ter ficado 30 minutos só tentando fazer isso funcionar, me sinto realizado

def transfDict(aDict, gridSize): # transforma o dict da função acima em uma tuple final
    return tuple(tuple(aDict[(x, y)].pop() for x in range(0, gridSize)) for y in range(0, gridSize))

# VALIDANDO OBJETOS
def validateRows(possibX): # valida linhas
    return [tuple(filter(lineValid, rC)) for rC in possibX]

def validateRow(y, aPoss, leftRight, gridSize): # valida linha
    possibRowPermutations = makeRows(y=y, aPoss=aPoss, gridSize=gridSize)
    l, r = leftRight[y]
    return [rowC for rowC in possibRowPermutations if lineWBoundsPossib(rowC, l, r)]

def validateColumns(possibX): # valida colunas
    return [tuple(filter(lineValid, cC)) for cC in possibX]

def validateColumn(x, aPoss, topBottom, gridSize): # valida coluna
    possibColumnPermutations = makeColumns(x=x, aPoss=aPoss, gridSize=gridSize)
    t, b = topBottom[x]
    return [columnC for columnC in possibColumnPermutations if lineWBoundsPossib(columnC, t, b)]

def validateSLines(sLinesC, gridSize): # valida os lados de cada linha
    return [validateLines(lineCC, gridSize) for lineCC in  sLinesC]

def validateLines(lineCC, gridSize): # valida as linhas
    llv = lambda x: lineValid(x, gridSize)
    return [tuple(filter(llv, lineC)) for lineC in lineCC]

def checkA(aDict, gridSize): # checa a resposta, ou seja, a length
    return len({len(aDict[(x, y)]) for x in range(0, gridSize) for y in range(0, gridSize)}) == 1

# RESOLVER FINALMENTE
def solve(clues, gridSize = 6): # FINALMENTE AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    visPosList = visualPossib(gridSize)
    top, right, bottom, left = treatClue(clues, gridSize)

    right, cLeft = right, list(reversed(left))
    lr = list(zip(cLeft, right))

    top, cBottom = top, list(reversed(bottom))
    tb = list(zip(top, cBottom))

    cells = {(x, y) for y in range(0, gridSize) for x in range(0, gridSize)}

    possibR = [possibLines(x, y, visPosList) for x, y in lr]
    possibC = [possibLines(x, y, visPosList) for x, y in tb]

    dictPossibV = makeDictPossibRC(possibR, possibC, cells)

    validatedR, validatedC = splitDictRC(dictPossibV, gridSize)

    rDictPossibV = makeDictPossibRC(validatedR, validatedC, cells)

    for _ in range(50):
        revalidatedR, revalidatedC = splitDictRC(rDictPossibV, gridSize)
        
        revalidatedR = [[rC for rC in possibRPermutations if lineWBoundsPossib(rC, l, r)] for possibRPermutations, l, r in zip(revalidatedR, cLeft, right)]
        revalidatedC = [[cC for cC in possibCPermutations if lineWBoundsPossib(cC, t, b)] for possibCPermutations, t, b in zip(revalidatedC, top, cBottom)]
        newRDictPossibV = makeDictPossibRC(revalidatedR, revalidatedC, cells)

        if checkA(rDictPossibV, gridSize):
            break
        elif newRDictPossibV == rDictPossibV:
            raise Exception("Problemas no processo de solução!")
        else:
            rDictPossibV = newRDictPossibV
    
    resultado = transfDict(rDictPossibV, gridSize)
    return resultado

def solve_puzzle(clues):
    return solve(clues)

clues = ( 3, 2, 2, 3, 2, 1,
          1, 2, 3, 3, 2, 2,
          5, 1, 2, 2, 4, 3,
          3, 2, 1, 2, 2, 4)

print(solve_puzzle(clues))
