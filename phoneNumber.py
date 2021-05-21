# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) #"(123) 456-7890"
# create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) #"(111) 111-1111"
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) #"(123) 456-7890"
# create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]) #"(023) 056-0890"
# create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) #"(000) 000-0000"

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 0] => "(123) 456-7890"

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))