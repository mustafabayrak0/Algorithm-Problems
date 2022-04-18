roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def convert(x: str):
    sum = 0
    temp_sum = 0
    if len(x) > 1:
        for i in range(len(x) - 1):
            if roman[x[i + 1]] <= roman[x[i]]:
                temp_sum += roman[x[i]]
            elif roman[x[i + 1]] > roman[x[i]]:
                temp_sum -= roman[x[i]]
            sum = temp_sum + roman[x[len(x) - 1]]
        return sum
    elif len(x) == 1:
        return roman[x[0]]
    else:
        return "BOŞ"


user_input = input()
print(convert(user_input))
