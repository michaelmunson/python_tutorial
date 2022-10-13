# test if someone is a human or not

# ...
user_input = input("Are you a human? [y/N]\n")

if user_input == "y":
    print("You are a human!")

elif ("y" in user_input) or ("j" in user_input) or ("santa claus" in user_input):
    print("there is a 'y' in the statement")

elif user_input == "n":
    print("Get off my screen you dirty bot!")

elif user_input == "q":
    print("Read directions again you blind maggot (hint: only 'y' or 'n') !!!!")

else:
    print("Please try again...")


