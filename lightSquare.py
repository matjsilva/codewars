# list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]
# list_squared(42, 250), [[42, 2500], [246, 84100]]
# list_squared(250, 500), [[287, 84100]]

# 1 <= m <= n

# encontre todos inteiros entre m e n, em que a soma de seus divisores elevados ao quadrado é o próprio inteiro elevado ao quadrado

import math

def light_squared(m, n):
    finalArray = [] # array mostrado no final do código
    if m >= 1 and n >= m: # condição inicial
        for num in range(m, n + 1): # organizando o ambiente para valores mais precisos e maior velocidade do código
            divs = set() # set() pois preciso armazenar vários valores iteráveis distintos em uma só variável
            for i in range(1, int(math.sqrt(num)+1)): # range dos divisores, requer raíz quadrada do número para maior velocidade do código
                if num % i == 0: # condição dos divisores
                    divs.add(i**2) # adicionando divisores quadrados
                    divs.add(int(num/i)**2) # o valor da divisão da prova real quadrado a lista dos divisores
            sumDivs = sum(divs) # somando os divisores
            sqrtDivs = math.sqrt(sumDivs) # raíz quadrada dos divisores para usar na condição final
            if sqrtDivs - math.floor(sqrtDivs) == 0: # condição final, provando que a raiz quadrada dos divisores é um quadrado perfeito
                finalArray.append([num, sumDivs]) # FINALMENTE CRL
    return finalArray # :)

print(light_squared(1, 250))