# A program to convert string to list by removing all the white spaces and also if digit in the list is greater than 5 remove it, otherwise keep it. 

def str_to_list (str):
    char=list(str)
    for space in char:
        if space == ' ':
            char.remove(space)
    for digit in char:
        if digit.isdigit() and int(digit) > 5:
            char.remove(digit)
    return char

print (str_to_list("my string"))
print (str_to_list("5 string"))
print (str_to_list("6 string"))
print (str_to_list("7 dollars"))
print (str_to_list("6 cents"))