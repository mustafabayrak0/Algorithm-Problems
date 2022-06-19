count = 0
user_inp = input()
user_input = user_inp[1:len(user_inp) - 1]
short = False
if len(user_input) < 6:
    short = True

long = False
if len(user_input) > 20:
    long = True

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digit_control = True
for i in user_input:
    if i in digits:
        digit_control = False
        break

upper_control = True
for i in user_input:
    if i.isupper():
        upper_control = False
        break

lower_control = True
for i in user_input:
    if i.islower():
        lower_control = False
        break

counter = 1
counts_list = []
repeat_control = False
if len(user_input) >= 3:
    for i in range(1, len(user_input)):
        if user_input[i - 1] == user_input[i]:
            counter += 1
            if counter >= 3 and i == len(user_input) - 1:
                counts_list.append(counter)
        else:
            if counter >= 3:
                counts_list.append(counter)
            counter = 1
        if len(counts_list) > 0:
            repeat_control = True
# 1.
if not short and not long and not repeat_control:
    lst = [lower_control, digit_control, upper_control]
    for i in lst:
        if i is True:
            count += 1
# 2.
if short and not repeat_control:
    temp = 0
    diff = 6 - len(user_input)
    lst = [lower_control, digit_control, upper_control]
    for i in lst:
        if i is True:
            temp += 1
    if diff >= temp:
        count += diff
    else:
        count += (diff + (temp - diff))
# 3.
if long and not repeat_control:
    temp = 0
    diff = len(user_input) - 20
    lst = [lower_control, digit_control, upper_control]
    for i in lst:
        if i is True:
            temp += 1
    count += diff + temp
# 4.
if short and repeat_control:
    temp = 0
    change = 0
    diff = 6 - len(user_input)
    lst = [lower_control, digit_control, upper_control]
    for i in lst:
        if i is True:
            temp += 1
    for i in counts_list:
        change += i // 3
    count += diff
    lsst = [change, temp]
    if diff >= max(lsst):
        pass
    else:
        count += max(lsst) - diff

# 5.
if long and repeat_control:
    temp = 0
    change = 0
    diff = len(user_input) - 20
    lst = [lower_control, digit_control, upper_control]
    for i in lst:
        if i is True:
            temp += 1
    for i in counts_list:
        change += int(i // 3)
    del_change = 0
    for i in counts_list:
        del_change += i - 2
    del_change -= diff
    if temp == 0:
        count += diff
        counts_list.sort()
        while diff > 0:
            for i in range(len(counts_list)):
                k = int(counts_list[i])
                k -= 1
                counts_list[i] = k
                diff -= 1
        if del_change > 0:
            for i in counts_list:
                count += i // 3

    else:
        change_updated = 0
        count += diff
        counts_list.sort()
        while diff > 0:
            for i in range(len(counts_list)):
                k = int(counts_list[i])
                k -= 1
                counts_list[i] = k
                diff -= 1
        for i in counts_list:
            change_updated += i // 3
        count += change_updated
        if temp > change_updated:
            count += temp - change_updated

# 6.
if not short and not long and repeat_control:
    lst = [lower_control, digit_control, upper_control]
    change = 0
    temp = 0
    for i in lst:
        if i is True:
            temp += 1
    for i in counts_list:
        change += i // 3
    if temp >= change:
        count += temp
    else:
        count += change
print(count)
