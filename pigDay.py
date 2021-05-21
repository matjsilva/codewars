# pig_it('Pig latin is cool'),'igPay atinlay siay oolcay'
# pig_it('This is my string'),'hisTay siay ymay tringsay'

def pig_it(text):
    resultado = ""
    resultadoList = []

    for word in text.split():
        if word == "?" or word == "!":
            pass
        else:
            word = word[1:] + word[0] + "ay"
        resultadoList.append(word)
    
    resultado = " ".join(resultadoList)
    return resultado

print(pig_it("Quis custodiet ipsos custodes !"))


