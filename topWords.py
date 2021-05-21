# top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"]
# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"]
# top_3_words("  //wont won't won't "), ["won't", "wont"]
from collections import Counter
import re

def top_3_words(text):
    resultado = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    return [w for w,_ in resultado.most_common(3)]

print(top_3_words("b b b b b  b bb  b bb b b b b b b b b  b b b b  b b b b dd d d d  d a b n md PpP"))

# rank = {}
# a = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", 'k', "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# for word in text.lower().split():
#     word = word.replace(".","")
#     word = word.replace(",","")
#     word = word.replace(":","")
#     word = word.replace("\"","")
#     word = word.replace("/","")
#     word = word.replace("!","")
#     word = word.replace("â€œ","")
#     word = word.replace("â€˜","")
#     word = word.replace("?","")
#     word = word.replace("*","")
#     word = word.replace("_","")
#     word = word.replace("-","")
#     word = word.replace(";","")

#     if word != "" and :
#         if word not in rank:
#             rank[word] = 1
#         else:
#             rank[word] += 1

# preFinal = Counter(rank)
# final = preFinal.most_common(3)
# try:
#     return [f'{final[0][0]}', f'{final[1][0]}', f'{final[2][0]}']
# except IndexError:
#     try:
#         return [f'{final[0][0]}', f'{final[1][0]}']
#     except IndexError:
#         try:
#             return [f'{final[0][0]}']
#         except IndexError:
#             return []