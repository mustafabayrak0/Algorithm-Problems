shel = int(input())
lst = input()
for i in lst:
    lst = lst.replace("[[", "")
    lst = lst.replace("]]", "")
    lst = lst.replace("]", "")
    lst = lst.replace("[", "")
lst2 = lst.split(",")
restr_lst = []
for j in range(len(lst2) - 1):
    restr_lst.append([int(lst2[j]), int(lst2[j + 1])])
restr_lst_last = []
for i in range(len(restr_lst)):
    if i % 2 == 0:
        restr_lst_last.append(restr_lst[i])

last_restrict = []
for i in range(shel):
    last_restrict.append(i)
for i in range(len(restr_lst_last)):
    for j in range(len(last_restrict)):
        if restr_lst_last[i][0] - 1 == j and restr_lst_last[i][1] < restr_lst_last[i][0] - 1:
            last_restrict[j] = restr_lst_last[i][1]


def conroller(a, b, c):
    for i in range(a, b, c):
        mx_lst = [last_restrict[i - 1], last_restrict[i + 1]]
        mx = max(mx_lst)
        mn = min(mx_lst)
        if abs(last_restrict[i - 1] - last_restrict[i + 1]) == 0:
            if mx + 1 <= last_restrict[i]:
                last_restrict[i] = mx + 1
        elif abs(last_restrict[i - 1] - last_restrict[i + 1]) == 1:
            if mx <= last_restrict[i]:
                last_restrict[i] = mx
        elif abs(last_restrict[i - 1] - last_restrict[i + 1]) == 2:
            if mx <= last_restrict[i]:
                last_restrict[i] = mx
        else:
            if mn + 1 <= last_restrict[i]:
                last_restrict[i] = mn + 1
        if last_restrict[-1] > last_restrict[-2]:
            last_restrict[-1] = last_restrict[-2] + 1


conroller(2, len(last_restrict) - 1, 1)
conroller(len(last_restrict) - 2, 1, -1)
print(max(last_restrict))
