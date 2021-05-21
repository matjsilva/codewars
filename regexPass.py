# search(regex, 'fjd3IR9'), True
# search(regex, 'ghdfj32'), False

import re

# regex = "^[A-Za-z0-9]{6,}$" | primeiro teste, deu certo... ou quase
# regex = "[A-Z0-9]*(?![a-z]){6,}$" | segundo teste, mesma coisa do primeiro
# regex = "[A-Za-z0-9@#$%^&+=]{6,}" | terceiro, chegando cada vez mais perto
# regexProto = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6}$" | quarto, MUITO perto
regexProto = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])[A-Za-z0-9]{6}$" #| ultimo teste, DEU CERTO
regex = re.compile(regexProto)

print("Teste da string fjd3IR9 [True]:", bool(re.search(regex, "fjd3IR9")))
print("Teste da string ghdfj32 [False]:", bool(re.search(regex, "ghdfj32")))
print("Teste da string 123 [False]:", bool(re.search(regex, "123")))