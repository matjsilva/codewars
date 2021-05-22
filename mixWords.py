# mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr"
# mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'

# s1, s2
# apenas levar em consideração letras em minúsculo (a-z) | regex!
# mostrar qual a maior diferença entre s1 e s2 como:
#   1:nw/2:nw - diferença
#    :=nw     - igualdade, mesmo max em s1 e s2

# import re

def mix(s1, s2):
    # s1lc = re.findall("[a-z]+", s1) | a ideia do regex era boa, até eu perceber que tenho que checar letra por letra do alfabeto, mas não sou bom o bastante ainda pra coletar as letras do regex [a-z], então vou usar uma string com as letras do alfabeto mesmo, é isso.

    sDict = {}
    for l in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(l), s2.count(l)
        if max(val1, val2) > 1:
            j = "1" if val1 > val2 else "2" if val2 > val1 else "=" # sinceramente, to com muito sono pra explicar essa operação ternária, e eu nem sei se ta certo | edit: ta certo.
            sDict[l] = (-max(val1, val2), j + ":" + l * max(val1, val2))
    return "/".join(sDict[l][1] for l in sorted(sDict, key=lambda x: sDict[x])) # no geral, eu junto o resultado do j+sDict[l], que nada mais é que as letras só que bem automatizado e encurtado (bem dita seja a operação ternária), to feliz com o resultado. 


mix("Are they HERE", "kek")
