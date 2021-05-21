# expanded_form(12), '10 + 2'
# expanded_form(70304), '70000 + 300 + 4'

def expanded_form(num):
    # i => num[i]
    # digito => str(num)
    # manipulo as posições e multiplico pelo i
    
    resultado = []

    for i, digito in enumerate(str(num)[::-1]):
        if int(digito) != 0:
            resultado.append(digito + ('0' * i))

    return " + ".join(resultado[::-1])
