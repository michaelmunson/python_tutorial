# while loops

# add 10 to each item in list
int_list = [0,3,2,10,124,13]

index = 0

while index < len(int_list):
    int_list[index] = int_list[index] + 10
    index = index + 1

print(int_list)