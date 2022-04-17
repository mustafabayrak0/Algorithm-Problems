user_input=input()
new_string2 = ""
new_string3 = ""
def length_function(m:str):
    length = 0
    for i in m:
        length+=1
    return length
for i in user_input:
    new_string3 += i + " "
for k in range(0, length_function(new_string3) - 1, 1):
    new_string2 += new_string3[k]
def recursive_reversed_string_printing (x:str):
    y = length_function(new_string2)
    if (length_function(user_input) >= 10):
        return print("Too Long Input")
    else:
        if(length_function(x)==0):
            return ""
        else:
            return  print(f"{x[::-1]} {(int((((y-length_function(x))+1)/2)+1) * ('* '))}"),recursive_reversed_string_printing (x[2:])
recursive_reversed_string_printing(new_string2)
