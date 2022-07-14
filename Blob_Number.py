# Name:Mustafa Bayrak
# Id: 150210339

# I numbered the blobs and then checked
def around_checker(row_index, column_index, grid: list):
    lst = []
    try:
        for i in [grid[row_index - 1][column_index], grid[row_index + 1][column_index],
                  grid[row_index][column_index - 1], grid[row_index][column_index + 1]]:
            if i != '':
                lst.append(i)
    except Exception as err:
        pass
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
filled_list.sort()  # sort the filled list
for i in grid:
    for j in i:
        print(j, end="")  # printing grid
    print("\r")

for t in filled_list:
    i, j = t[0], t[1]
    l = []
    lst = around_checker(i, j, grid)
    int_check = False
    character_check = False
    for k in lst:
        if type(k) is int:
            int_check = True
            break
        elif k == character:
            character_check = True
    if int_check:
        for f in lst:
            if type(f) is int:
                l += [f]
        grid[i][j] = min(l)
    elif not int_check and character_check:
        result += 1
        grid[i][j] = result
    else:
        result += 1
        grid[i][j] = result


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
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # First row excluding first column and last column
                elif r == 0 and 0 < c < column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # upper left corner
                elif r == 0 and c == 0:
                    lst = [grid[r][c + 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # bottom row but excluding first and last column
                elif r == row_number - 1 and c != 0 and c != column_number - 1:
                    lst = [grid[r][c + 1], grid[r][c - 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # bottom left corner
                elif r == row_number - 1 and c == 0:
                    lst = [grid[r][c + 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # last column but excluding first and last row
                elif c == column_number - 1 and r != row_number - 1 and r != 0:
                    lst = [grid[r][c - 1], grid[r + 1][c], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # top right corner
                elif c == column_number - 1 and r == 0:
                    lst = [grid[r][c - 1], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                # bottom right corner
                elif c == column_number - 1 and r == row_number - 1:
                    lst = [grid[r][c - 1], grid[r - 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
                    else:
                        grid[r][c] = result
                #  first column but excluding first and last row
                elif c == 0 and r != row_number - 1 and r != 0:
                    lst = [grid[r][c + 1], grid[r - 1][c], grid[r + 1][c], grid[r][c]]
                    for k in lst:
                        if type(k) is int:
                            l += [k]
                    if len(l) != 0:
                        grid[r][c] = min(l)  # find the smallest number around
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
count = len(result_set)
print(count)

#Sample Input 
# 3 11
# *
# 12  
# 0 2
# 0 3
# 0 6
# 0 4
# 0 7
# 0 8
# 1 4
# 1 8
# 1 6
# 2 6
# 2 5
# 2 4
