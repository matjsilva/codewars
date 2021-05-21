# RomanNumerals.to_roman(1000), 'M'
# RomanNumerals.to_roman(1990), 'MCMXC'

class RomanNumerals:
    def __init__(self, value):
        self.value = value

    def from_roman(value):
        # posição1 posição2
        #    I    -   V
        #    I    +   I
        # se posição1 < posição2
        #    posição2 - posição1
        # se posição1 >= posição2
        #    posição2 + posição1

        charList = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900
        }

        resultado = 0
        i = 0

        while i < len(value):
            if i+1<len(value) and value[i:i+2] in charList:
                resultado += charList[value[i:i+2]]
                i += 2
            else:
                resultado += charList[value[i]]
                i += 1
        
        return resultado

    def to_roman(dec):
        # agora, é sobre posições, eu acho.
        # decList[i] == charList[i] => decList[i] = 1000 == charList[i] = 'M'
        # decList   :  pos
        # charList  :  pos
        # -----------------
        # resultado | simbolo

        # esse é bem simples na verdade, mais fácil que o from_roman
        # é só ir adicionando os correspondentes, nada demais

        decList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        charList = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        resultado = ""
        i = 0

        while dec > 0:
            for n in range(dec // decList[i]):
                resultado += charList[i]
                dec -= decList[i]
            i += 1

        return resultado     
        

# TESTES

print(RomanNumerals.from_roman("VII"))
print(RomanNumerals.to_roman(4))