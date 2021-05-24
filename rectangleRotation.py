# rectangle_rotation(6,4),23
# rectangle_rotation(30,2),65

# trata-se de um retângulo em um plano cartesianno rotacionado em 45° com a intersecção de suas diagonais (ou seja, seu centro) na coordenada 0,0
# descobrir quantos plots com coordenadas no conjunto dos números inteiros do gráfico estão dentro do retângulo

# regras
# ------
# [input] integer a
# A positive even integer.
# Constraints: 2 ≤ a ≤ 10000.

# [input] integer b
# A positive even integer.
# Constraints: 2 ≤ b ≤ 10000.

# [output] an integer

# The number of inner points with integer coordinates.

# ok, pra esse código tive 2 ideias, uma envolve trigonometria e a outra matplotlib
# esse desafio teve uma relação muito mais forte com matemática do que programação, então muito do que eu anotei não tá comentado como eu costumo fazer, mas sim no papel.
# cálculos... alias, eu disse que faria com matplotlib ou trigonometria, acabei fazendo com o método k-d tree, um método de algoritmo usado em computação.

import math
import numpy as np

def rectangle_rotation(a, b):
    # é só uma divisão do retangulo pela raiz de 2 / 2, trigonometria, mas tudo tem um porque
    aHB = (a/math.sqrt(2))/2
    bHB = (b/math.sqrt(2))/2

    # listas que vão abrigar os bisetores, com valores arredondados, pois preciso de valores inteiros, *2 pois é uma bisseção, +1, assim incluindo o ponto na origem
    rec1 = [math.floor(aHB)*2+1, math.floor(bHB)*2+1]
    rec2 = []

    # testes que decidem se o ponto está dentro do retangulo, ou não
    if aHB - math.floor(aHB) < 0.5:
        rec2.append(rec1[0]-1)
    else:
        rec2.append(rec1[0]+1)
    
    if bHB - math.floor(bHB) < 0.5:
        rec2.append(rec1[1]-1)
    else:
        rec2.append(rec1[1]+1)
    
    # multiplicação dos elementos da lista por si mesmos para gerar a quantidade de pontos
    return np.prod(rec1) + np.prod(rec2)

    # tringonometria
    # --------------
    # aL = a/2
    # bL = b/2
    # cL = aL/-2
    # aL2 = aL*math.cos(-45) - bL*math.sin(-45)
    # bL2 = aL*math.sin(-45) + bL*math.cos(-45)
    # cL2 = cL*math.cos(-45) - bL*math.cos(-45)

    # matplotlib
    # ----------
    # recFig = plt.figure()
    # recAx = recFig.add_subplot(111)

    # rec = patches.Rectangle((0, 0), a, b, 0)

    # st = recAx.transData
    # t = mpl.transforms.Affine2D().rotate_deg(-45)
    # r = st + t

    # rec.set_transform(r)

    # recAx.add_patch(rec)
    # plt.grid()
    # plt.show()

print(rectangle_rotation(6, 4))
