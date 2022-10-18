# while loops

# add 10 to each item in list
int_list = [0,3,2,10,124,7]

index = 0

# while loop runs forever because index is never incremented
while index < len(int_list):
    int_list[index] = int_list[index] + 10

print(int_list)