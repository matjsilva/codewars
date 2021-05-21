# I = [12, 15] | sum_for_list(a), [[2, 12], [3, 27], [5, 15]]
# I = [15, 21, 24, 30, 45] | sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]]

# I = [i1, .., in] | P = [[p | p é a soma de todos os ij de I para qual p é um fatorial primo (positivo)de ij], ...]

# encontrar os fatoriais primos
# combinar os dados
# retornar

def primeFactor(n): # encontrando os fatoriais primos
    i = 2
    n = abs(n)
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

    # antiga resolução, overengineering
    # ----------------------
    # if n < 0:
    #     n *= n-1
    # while i * i <= n:
    #     if n % i:
    #         i += 1
    #     else:
    #         n //= i
    #         factors.append(i)
    # if n > 1:
    #     factors.append(n)
    # return factors

# não será mais necessário
# ------------------------
# def arrange(arr1, arr2): # combinando dados
#     for j in arr1:
#         if not j in arr2:
#             arr2.append(j)
#     return arr2

def sum_for_list(lst):
    factors = []
    resultado = []
    for n in lst:
        factors = list(set(factors).union(set(primeFactor(n))))
    factors.sort()
    for n in factors:
        sum = 0
        lstN = [n]
        for i in lst:
            if i%n == 0:
                sum += i
        lstN.append(sum)
        resultado.append(lstN)
    return resultado

    # antiga resolução, possuía erros de combinatória
    # -----------------------------------------------
    # sums = []
    # for i in range(len(lst)):
    #     arrange(primeFactor(lst[i]), factors)
    # for i in range(len(factors)):
    #     sum = 0
    #     for n in range(len(lst)):
    #         if not lst[n]%factors[i]:
    #             sum += lst[n]
    #     sums.append([factors[i], sum])
    # sums.sort(key=lambda factors:factors[0])
    # return sums
