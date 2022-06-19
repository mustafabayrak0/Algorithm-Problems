# Name:Mustafa Bayrak
# Id: 150210339

# I numbered the blobs and then checked

# finds length
def length_function(m):
    length = 0
    for i in m:
        length += 1
    return length


# finds min element
def find_min(lst):
    if length_function(lst) == 0:
        return None
    min_res = lst[0]
    for i in lst:
        if i < min_res:
            min_res = i
    return min_res


# sorts list
def sort_lst(lst):
    for i in range(length_function(lst)):
        for j in range(length_function(lst) - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


row_number, column_number = map(int, input().split())  # row number and column number inputs
character = input()  # character input
filled_character_number = int(input())  # number of filled characters

grid = []
result = 0

# {row_number}x{column_number} matrix
for i in range(row_number):
    temp_lst = []
    for j in range(column_number):
        temp_lst += [" "]
    grid += [temp_lst]  # creating grid with empty cells

filled_list = []

# filling cells of grid
for i in range(filled_character_number):
    filled_row, filled_column = map(int, input().split())  # take input of filled cells
    filled_list += [[filled_row, filled_column]]  # add filled ones to a list
    grid[filled_list[i][0]][filled_list[i][1]] = character  # define character
sort_lst(filled_list)  # sort the filled list
for i in grid:
    for j in i:
        print(j, end="")  # printing grid
    print("\r")

for i in filled_list:
    r, c = i[0], i[1]
    l = []
    # except borders
    if 0 < r < row_number - 1 and 0 < c < column_number - 1:
        if type(grid[r][c + 1]) is int or type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int or type(
                grid[r - 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r - 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r + 1][c] == character or \
                grid[r - 1][c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    #  First row excluding first column and last column
    elif r == 0 and 0 < c < column_number - 1:
        if type(grid[r][c + 1]) is int or type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int:
            lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c]]  # check if there are numbers around
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r + 1][
            c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    # upper left corner
    elif r == 0 and c == 0:
        if type(grid[r][c + 1]) is int or type(grid[r + 1][c]) is int:
            lst = [grid[r][c + 1], grid[r + 1][c]]  # check if there are numbers around
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c + 1] == character or grid[r + 1][c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    # bottom row but excluding first and last column
    elif r == row_number - 1 and c != 0 and c != column_number - 1:
        if type(grid[r][c + 1]) is int or type(grid[r][c - 1]) is int or type(
                grid[r - 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c + 1], grid[r][c - 1], grid[r - 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r - 1][
            c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    # bottom left corner
    elif r == row_number - 1 and c == 0:
        if type(grid[r][c + 1]) is int or type(grid[r - 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c + 1], grid[r - 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c + 1] == character or grid[r - 1][c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    # last column but excluding first and last row
    elif c == column_number - 1 and r != row_number - 1 and r != 0:
        if type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int or type(
                grid[r - 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c - 1], grid[r + 1][c], grid[r - 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c - 1] == character or grid[r + 1][c] == character or grid[r - 1][
            c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    # top right corner
    elif c == column_number - 1 and r == 0:
        if type(grid[r][c - 1]) is int or type(grid[r + 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c - 1], grid[r + 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c - 1] == character or grid[r + 1][c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    # bottom right corner
    elif c == column_number - 1 and r == row_number - 1:
        if type(grid[r][c - 1]) is int or type(grid[r - 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c - 1], grid[r - 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c - 1] == character or grid[r - 1][c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result
    #  first column but excluding first and last row
    elif c == 0 and r != row_number - 1 and r != 0:
        if type(grid[r][c + 1]) is int or type(grid[r - 1][c]) is int or type(
                grid[r + 1][c]) is int:  # check if there are numbers around
            lst = [grid[r][c + 1], grid[r - 1][c], grid[r + 1][c]]
            for k in lst:
                if type(k) is int:
                    l += [k]
            grid[r][c] = find_min(l)  # find the smallest number around
        elif grid[r][c + 1] == character or grid[r][c - 1] == character or grid[r + 1][
            c] == character:  # no numbers around, only characters
            result += 1
            grid[r][c] = result
        else:
            result += 1
            grid[r][c] = result


# In this function, it is checked whether the groups are numbered correctly.
def check_function(a, b, c, d, e, f):
    for r in range(a, b, c):
        for c in range(d, e, f):
            l = []
            if type(grid[r][c]) is int:
                # # except borders
                if 0 < r < row_number - 1 and 0 < c < column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # First row excluding first column and last column
                elif r == 0 and 0 < c < column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # upper left corner
                elif r == 0 and c == 0:
                    lst = [grid[r][c + 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # bottom row but excluding first and last column
                elif r == row_number - 1 and c != 0 and c != column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # bottom left corner
                elif r == row_number - 1 and c == 0:
                    lst = [grid[r][c + 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # last column but excluding first and last row
                elif c == column_number - 1 and r != row_number - 1 and r != 0:
                    lst = [grid[r][c - 1], grid[r + 1][c], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # top right corner
                elif c == column_number - 1 and r == 0:
                    lst = [grid[r][c - 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # bottom right corner
                elif c == column_number - 1 and r == row_number - 1:
                    lst = [grid[r][c - 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                #  first column but excluding first and last row
                elif c == 0 and r != row_number - 1 and r != 0:
                    lst = [grid[r][c + 1], grid[r - 1][c], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if length_function(l) != 0:
                        grid[r][c] = find_min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
    return grid


# checking numbers in different directions
check_function(row_number - 1, -1, -1, column_number - 1, -1, -1)
check_function(0, row_number, 1, column_number - 1, -1, -1)
check_function(row_number - 1, -1, -1, 0, column_number, 1)
check_function(0, row_number, 1, 0, column_number, 1)

result_set = set()
for i in grid:
    for j in i:
        if type(j) is int:
            result_set.add(j)  # add to the set to find out how many different groups there are
count = length_function(result_set)
print(count)
