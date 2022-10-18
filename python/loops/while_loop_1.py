
my_string = "ABCDEFGHIJKLMN"

cond = True
iter = 0

while cond:
    letter = my_string[iter]
    iter = iter + 1
    if letter == "G":
        cond = False
    print(letter)