row_number, column_number = map(int, input().split())  # row number and column number inputs
character = input()  # character input
filled_character_number = int(input())  # number of filled characters

grid = []
result = 0

# {row_number}x{column_number} matrix
for i in range(row_number):
    temp_lst = []
    for j in range(column_number):
        temp_lst.append(" ")
    grid.append(temp_lst)

filled_list = []

# filling cells of grid
for i in range(filled_character_number):
    filled_row, filled_column = map(int, input().split())
    filled_list.append([filled_row, filled_column])
    grid[filled_list[i][0]][filled_list[i][1]] = character
filled_list.sort()
for i in grid:
    for j in i:
        print(j, end="")
    print("\r")

for i in range(len(filled_list)):
    r, c = filled_list[i][0], filled_list[i][1]
    l = []
    if grid[r][c] == character:
        # sinir haric
        if 0 < r < row_number - 1 and 0 < c < column_number - 1:
            if type(grid[r][c + 1]) is int or type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int or type(
                    grid[r - 1][c]) is int:
                lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r - 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r + 1][c] == character or \
                    grid[r - 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # ilk satir ama ilk sutun ve son sutun harici



        elif r == 0 and 0 < c < column_number - 1:
            if type(grid[r][c + 1]) is int or type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int:
                lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r + 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # sol ust kose
        elif r == 0 and c == 0:
            if type(grid[r][c + 1]) is int or type(grid[r + 1][c]) is int:
                lst = [grid[r][c + 1], grid[r + 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c + 1] == character or grid[r + 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # en alt satir ama ilk ve son sutun haric
        elif r == row_number - 1 and c != column_number - 1:
            if type(grid[r][c + 1]) is int or type(grid[r][c - 1]) is int or type(grid[r - 1][c]) is int:
                lst = [grid[r][c + 1], grid[r][c - 1], grid[r - 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r - 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # sol en alt kose
        elif r == row_number - 1 and c == 0:
            if type(grid[r][c + 1]) is int or type(grid[r - 1][c]) is int:
                lst = [grid[r][c + 1], grid[r - 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c + 1] == character or grid[r - 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # son sutun ama ilk ve son satir haric
        elif c == column_number - 1 and r != row_number - 1 and r != 0:
            if type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int or type(grid[r - 1][c]) is int:
                lst = [grid[r][c - 1], grid[r + 1][c], grid[r - 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c - 1] == character or grid[r + 1][c] == character or grid[r - 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # en ust sag kose
        elif c == column_number - 1 and r == 0:
            if type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int:
                lst = [grid[r][c - 1], grid[r + 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c - 1] == character or grid[r + 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # en alt sag kose
        elif c == column_number - 1 and r == row_number - 1:
            if type(grid[r][c - 1]) is int or type(grid[r - 1][c]) is int:
                lst = [grid[r][c - 1], grid[r - 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c - 1] == character or grid[r - 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result
        # ilk sutun ama ilk ve son satir haric
        elif c == 0 and r != row_number - 1 and r != 0:
            if type(grid[r][c + 1]) is int or type(grid[r - 1][c]) is int or type(grid[r + 1][c]) is int:
                lst = [grid[r][c + 1], grid[r - 1][c], grid[r + 1][c]]
                for k in lst:
                    if type(k) is int:
                        l.append(k)
                grid[r][c] = min(l)
            elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r + 1][c] == character:
                result += 1
                grid[r][c] = result
            else:
                result += 1
                grid[r][c] = result


def check_function(a, b, c, d, e, f):
    for r in range(a, b, c):
        for c in range(d, e, f):
            l = []
            if type(grid[r][c]) is int:
                # sinir haric
                if 0 < r < row_number - 1 and 0 < c < column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # ilk satir ama ilk sutun ve son sutun harici
                elif r == 0 and 0 < c < column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # sol ust kose
                elif r == 0 and c == 0:
                    lst = [grid[r][c + 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # en alt satir ama ilk ve son sutun haric
                elif r == row_number - 1 and c != column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # sol en alt kose
                elif r == row_number - 1 and c == 0:
                    lst = [grid[r][c + 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # son sutun ama ilk ve son satir haric
                elif c == column_number - 1 and r != row_number - 1 and r != 0:
                    lst = [grid[r][c - 1], grid[r + 1][c], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # en ust sag kose
                elif c == column_number - 1 and r == 0:
                    lst = [grid[r][c - 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # en alt sag kose
                elif c == column_number - 1 and r == row_number - 1:
                    lst = [grid[r][c - 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
                # ilk sutun ama ilk ve son satir haric
                elif c == 0 and r != row_number - 1 and r != 0:
                    lst = [grid[r][c + 1], grid[r - 1][c], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l.append(k)
                    if len(l) != 0:
                        grid[r][c] = min(l)
                    else:
                        grid[r][c] = result
    return grid


check_function(row_number - 1, -1, -1, column_number - 1, -1, -1)
check_function(0, row_number, 1, column_number - 1, -1, -1)
check_function(row_number - 1, -1, -1, 0, column_number, 1)
check_function(0, row_number, 1, 0, column_number, 1)

result_set = set()
for i in grid:
    for j in i:
        if type(j) is int:
            result_set.add(j)
count = len(result_set)
print(count)
