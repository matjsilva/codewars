# 0 = not interesting
# 1 = interesting number coming in the next two miles
# 2 = interesting

# Any digit followed by all zeros: 100, 90000
# Every digit is the same number: 1111
# The digits are sequential, incementing†: 1234
# The digits are sequential, decrementing‡: 4321
# The digits are a palindrome: 1221 or 73837
# The digits match one of the values in the awesome_phrases array

# is_interesting(3, [1337, 256])    # 0
# is_interesting(3236, [1337, 256]) # 0
# is_interesting(11207, []) # 0
# is_interesting(11208, []) # 0
# is_interesting(11209, []) # 1
# is_interesting(11210, []) # 1
# is_interesting(11211, []) # 2

# final; criada em 30-40 minutos
def is_interesting(number, awesome_phrases):
    for j, n in zip((2, 1, 1), range(number, number+3)):
        nStr = str(n)
        if n in awesome_phrases or n > 99 and (int(nStr[1:]) == 0 or nStr[::-1] == nStr or nStr in '1234567890' or nStr in '9876543210'):
            return j
    return 0

# almost good; criada em 20 minutos
# --------------------
# def numAwesome(n, awesome):
#     return n in awesome or str(n) in "1234567890 9876543210" or str(n) == str(n)[::-1] or int(str(n)[1:]) == 0
#
# def is_interesting(number, awesome_phrases):
#     if number > 99 and numAwesome(number, awesome_phrases):
#         return 2
#     if number > 97 and (numAwesome(number+1, awesome_phrases) or numAwesome(number+2, awesome_phrases)):
#         return 1
#     return 0

# proto version; criada em 5-10 minutos
# -------------------------------------
# if number > 1000:
#     if "0" in str(number)[0:]:
#         return "2"
#     elif str(number)[0] in str(number)[0:]:
#         return "2"
#     else:
#         for i in range(1, len(str(number))-1):
#             if str(number)[i] > str(number)[i-1]:
#                 return "2"
#             else:
#                 for i in range(len(str(number))-1, 1):
#                     if str(number)[i] < str(number)[i-1]:
#                         return "2"
#                     else:
#                         rev = 0
#                         j = number
#                         while(number>0):    
#                             dig = n%10
#                             rev = rev*10+dig
#                             n = n//10
#                         if(j==rev):
#                             return "2"
#                         else:
#                             return "0"
# else:
#     return "0"

print(is_interesting(3, [1337, 256])) # 0
print(is_interesting(11210, [])) # 1
print(is_interesting(11211, [])) # 2