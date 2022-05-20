def read_puzzle(): #this function reads puzzle
    result = []
    row_size, column_size = map(int, input().split())
    for i in range(row_size):
        puzzle_input = input().split()
        result.append(puzzle_input)
    return result


def read_words(): #this function reads words
    result = []
    word_number = int(input())
    for i in range(word_number):
        word_count, word_text = input().split()
        result.append(word_text)
    return result


def print_puzzle(puzzle): #this function prints puzzle
    for i in puzzle:
        print(' '.join(map(str, i)))


def print_words(words): #this function prints words
    for i in range(len(words)):
        print(str(i + 1) + "\t " + words[i]) #tab and space required


def horizontal_search(puzzle, word, puzzle_to_modify):
    temp_word = "" #to check word
    temp_word2 = "" #to check reverse word
    for i in range(len(puzzle[0])):
        k = 0
        d = 0
        while k <= len(puzzle[0]) - 1:
            if temp_word != word:
                if puzzle[i][k] == word[d]:
                    d += 1
                    temp_word += puzzle[i][k]

                else:
                    d = 0 #start again to check letters
                    temp_word = ""

            else:
                break
            row_end = i + 1 #variables used to find indexes
            column_end = k + 1
            row_first = row_end
            column_first = column_end + 1 - len(word)
            k += 1
    if temp_word == word:
        for j in range(column_first - 1, column_end):
            puzzle_to_modify[row_first - 1][j] = " " #replacing element
        print(word + f" found in horizontal search [{row_first}][{column_first}] to [{row_end}][{column_end}]")
    else: #checking reverse word
        for i in range(len(puzzle)):
            k = 0
            d = 1
            while k <= len(puzzle[0]) - 1:
                if temp_word2 != word[::-1]:
                    if puzzle[i][k] == word[-d]:
                        d += 1
                        temp_word2 += puzzle[i][k]
                    else:
                        d = 1 #last item's index is -1 so it should start with -1
                        temp_word2 = ""
                else:
                    break
                row_end = k + 1 #variables used to find indexes
                column_end = i + 1
                row_first = row_end + 1 - len(word)
                column_first = column_end
                k += 1

        if temp_word2 == word[::-1]: #if it is equal to reverse word
            for j in range(column_first - 1, column_end):
                puzzle_to_modify[row_first - 1][j] = " " #replacing element
            print(word + f" found in horizontal search [{column_end}][{row_end}] to [{column_first}][{row_first}]")

    return (temp_word == word or temp_word2 == word[::-1]), puzzle_to_modify #if temp_word or temp_word2 is correct


def vertical_search(puzzle, word, puzzle_to_modify):
    temp_word = "" #to check word
    temp_word2 = "" #to check reverse word
    for i in range(len(puzzle[0])):
        k = 0
        d = 0
        while k <= len(puzzle) - 1:
            if temp_word != word:
                if puzzle[k][i] == word[d]:
                    d += 1
                    temp_word += puzzle[k][i]
                else:
                    d = 0 #start again to check
                    temp_word = ""
            else:
                break
            row_end = k + 1 #variables used to find indexes
            column_end = i + 1
            row_first = row_end + 1 - len(word)
            column_first = column_end
            k += 1
    if temp_word == word:
        for j in range(row_first - 1, row_end):
            puzzle_to_modify[j][column_end - 1] = " " #replacing element
        print(word + f" found in vertical search [{row_first}][{column_first}] to [{row_end}][{column_end}]")
    else: #checking reverse word
        for i in range(len(puzzle[0])):
            k = 0
            d = 1
            while k <= len(puzzle) - 1:
                if temp_word2 != word[::-1]:
                    if puzzle[k][i] == word[-d]:
                        d += 1
                        temp_word2 += puzzle[k][i]
                    else:
                        d = 1
                        temp_word2 = ""
                else:
                    break
                row_end = k + 1 #variables used to find indexes
                column_end = i + 1
                row_first = row_end + 1 - len(word)
                column_first = column_end
                k += 1
        if temp_word2 == word[::-1]:
            for j in range(row_first - 1, row_end):
                puzzle_to_modify[j][column_end - 1] = " " #replacing element
            print(word + f" found in vertical search [{row_end}][{column_end}] to [{row_first}][{column_first}]")

    return (temp_word == word or temp_word2==word[::-1]), puzzle_to_modify


def diagonal_search(puzzle, word, puzzle_to_modify):
    temp_word = ""
    temp_word2=""
    for i in range(len(puzzle)): #down right
        k = 0
        d = 0
        a = i
        while k <= len(puzzle[0]) - 1:
            if temp_word != word:
                if puzzle[a][k] == word[d]:
                    temp_word += puzzle[a][k]
                    d += 1
                    a += 1
                    k += 1
                else:
                    d = 0
                    temp_word = ""
                    k += 1
                    a = i
            else:

                break
            row_end = a
            column_end = k
            row_first = row_end + 1 - len(word)
            column_first = column_end + 1 - len(word)
    if temp_word!=word:
        for i in range(len(puzzle)):  # down right
            k = 0
            d = 1
            a = i
            while k <= len(puzzle[0]) - 1:
                if temp_word2 != word[::-1]:
                    if puzzle[a][k] == word[-d]:
                        temp_word += puzzle[a][k]
                        d += 1
                        a += 1
                        k += 1
                    else:
                        d = 1
                        temp_word2 = ""
                        k += 1
                        a = i
                else:
                    break
                row_end = a
                column_end = k
                row_first = row_end + 1 - len(word)
                column_first = column_end + 1 - len(word)
    if temp_word != word:
        for i in range(len(puzzle)):# down left
            k = len(puzzle[0]) - 1
            d = 0
            a = i
            while k > 0:
                if temp_word != word:
                    if puzzle[a][k] == word[d]:
                        temp_word += puzzle[a][k]
                        d += 1
                        a += 1
                        k -= 1
                    else:
                        d = 0
                        temp_word = ""
                        k -= 1
                        a = i
                else:
                    break
                row_end = a
                column_end = k + 2
                row_first = row_end + 1 - len(word)
                column_first = column_end + len(word) - 1
    if temp_word != word:
        for i in range(len(puzzle)): #up right
            k = 0
            d = 0
            a = len(puzzle) - i - 1
            while k <= len(puzzle[0]) - 1:
                if temp_word != word:
                    if puzzle[a][k] == word[d]:
                        temp_word += puzzle[a][k]
                        d += 1
                        a -= 1
                        k += 1
                    else:
                        d = 0
                        if temp_word == "":  # check is it empty
                            k += 1
                        temp_word = ""
                        a = len(puzzle) - i - 1
                else:
                    break
                row_end = a + 2
                column_end = k
                row_first = row_end + len(word) - 1
                column_first = column_end - len(word) + 1
    if temp_word == word:
        if row_end > row_first and column_end > column_first:  # down,right move
            start_column = column_first - 1
            start_row = row_first - 1
            while start_column < len(puzzle[0]) - 1 and start_row < len(puzzle) - 1:
                puzzle_to_modify[start_row][start_column] = " "#replacing element
                start_row += 1
                start_column += 1
                if start_row == row_end - 1 and start_column == column_end - 1:
                    puzzle_to_modify[start_row][start_column] = " "#replacing element
                    break
        elif row_end > row_first and column_end < column_first:  # down,left move
            start_column = column_first - 1
            start_row = row_first - 1
            while start_column > 0 and start_row < len(puzzle) - 1:
                puzzle_to_modify[start_row][start_column] = " "#replacing element
                start_row += 1
                start_column -= 1
                if start_row == row_end - 1 and start_column == column_end - 1:
                    puzzle_to_modify[start_row][start_column] = " "#replacing element
                    break
        elif row_end < row_first and column_first < column_end:  # up,right move
            start_column = column_first - 1
            start_row = row_first - 1
            while start_column < len(puzzle[0]) - 1 and start_row > 0:
                puzzle_to_modify[start_row][start_column] = " "#replacing element
                start_row -= 1
                start_column += 1
                if start_row == row_end - 1 and start_column == column_end - 1:
                    puzzle_to_modify[start_row][start_column] = " "#replacing element
                    break
        elif row_end < row_first and column_first < column_end:  # up,left move
            start_column = column_first - 1
            start_row = row_first - 1
            while start_column > 0 and start_row > 0:
                puzzle_to_modify[start_row][start_column] = " " #replacing element
                start_row -= 1
                start_column -= 1
                if start_row == row_end - 1 and start_column == column_end - 1:
                    puzzle_to_modify[start_row][start_column] = " " #replacing element
                    break
        print(word + f" found in diagonal search [{row_first}][{column_first}] to [{row_end}][{column_end}]")
    return (temp_word == word), puzzle_to_modify



if __name__ == "__main__":
    puzzle = read_puzzle()
    words = read_words()
    print_puzzle(puzzle)
    print_words(words)
    puzzle_to_modify = [item.copy() for item in puzzle]
    for word in words:
        found, puzzle_to_modify = horizontal_search(puzzle, word, puzzle_to_modify)
        if not found:
            found, puzzle_to_modify = vertical_search(puzzle, word, puzzle_to_modify)
        if not found:
            found, puzzle_to_modify = diagonal_search(puzzle, word, puzzle_to_modify)

    print_puzzle(puzzle_to_modify)
#sample input
#15 15
# A S F G V E D H K L E R D G M
# K G V A N D E R V A L S S M A
# A C L M S R I I E E A L E N D
# Y D G A I S T P T E D T G R J
# L K J D E A G D O F A H E A U
# O L E C D A F M O L E K U L S
# U J L A L V I U A G D I A K K
# L N E J H H J S M H D I L M O
# S B M N A I B S K J H U P C V
# T V E A V D V I J R L K K O A
# B C N G T R N E O N U A F V L
# N E T F A O A R O W U E J Z E
# M W U U Y J M S L T S T U E N
# M D I I K E E A J S Z J Y G T
# A S L K L N V K G A C L K J K
# 9
# 1 KOVALENT
# 2 VANDERVALS
# 3 IYONIK
# 4 HIDROJEN
# 5 DIPOLDIPOL
# 6 ELEMENT
# 7 ATOM
# 8 MOLEKUL
# 9 METAL
