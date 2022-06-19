class Matrix:
    def __init__(self, m: int, n: int, values=None):
        self.m = m  # row
        self.n = n  # column
        self.values = values
        if m < 0 or n < 0:  # check if they are negative
            raise Exception(f"Matrix must have a positive dimension: mxn={m}x{n}")
        if values is None:  # if values parameter is None
            temp_list = []
            for i in range(m):
                temp_list.append(([float(item) for item in input().split()]))
                if len(temp_list[i]) != n:  # checking columns
                    raise Exception(f"You must enter n={n} number(s) in each row")
                    quit()  # quit if not enough input
            self.values = temp_list
            values = temp_list
            for i in self.values:
                if len(i) != n:  # checking columns
                    raise Exception(f"You must enter n={n} number(s) in each row")
        if values is not None:  # if values parameter is not None
            if type(values) is not list or [i for i in values if
                                            type(i) is not list]:  # checking if values is not list of list
                raise Exception("values parameter must be list of list")
            if len(values) != m:  # checking rows
                raise Exception(f"Number of rows in values must be equal to m={m}")
            for i in values:
                if len(i) != n:  # checking columns
                    raise Exception(f"Number of columns in values must be equal to n={n} in each row")

    def __str__(self):
        print(f"Matrix with {self.m}x{self.n} dimension")  # print dimension info
        for i in range(len(self.values)):
            for j in range(len(self.values[0])):
                print("{:10.3f}".format(float(self.values[i][j])), end="")  # printing elements of matrix
            if i < len(self.values) - 1:
                print("\r")  # carriage return
        return ""

    def __len__(self):
        return len(self.values)  # returns length

    def __sub__(self, other):
        if len(self.values) == len(other) and len(self.values[0]) == len(other.values[0]):  # checking dimensions
            result = []
            temp_row = []
            for i in range(len(self.values)):
                for j in range(len(self.values[0])):
                    temp_row.append(self.values[i][j] - other.values[i][j])  # subtraction
                result.append(temp_row)  # adds the rows of the result to the matrix
                temp_row = []
            add_matrix = Matrix(len(result), len(result[0]), result)
            return add_matrix
        else:
            raise Exception(
                f"Both matrices must have the same dimension.\nFirst: {self.m}x{self.n} Second: {len(other)}x{len(other.values[0])}")

    def __add__(self, other):
        if len(self.values) == len(other) and len(self.values[0]) == len(other.values[0]):  # checking dimensions
            result = []
            temp_row = []
            for i in range(len(self.values)):
                for j in range(len(self.values[0])):
                    temp_row.append(self.values[i][j] + other.values[i][j])  # addition
                result.append(temp_row)  # adds the rows of the result to the matrix
                temp_row = []
            add_matrix = Matrix(len(result), len(result[0]), result)
            return add_matrix
        else:
            raise Exception(
                f"Both matrices must have the same dimension.\nFirst: {self.m}x{self.n} Second: {len(other)}x{len(other.values[0])}")

    def transpose(self):
        matrix_t = [[self.values[j][i] for j in range(len(self.values))] for i in
                    range(len(self.values[0]))]  # row column interchange
        transpose_matrix = Matrix(len(matrix_t), len(matrix_t[0]), matrix_t)
        return transpose_matrix

    def __mul__(self, other):
        if type(other) is int or type(other) is float or type(other) is Matrix:
            if type(other) is int or type(other) is float:  # multiplication by an integer or a float
                result = []
                temp_row = []
                for i in range(len(self.values)):
                    for j in range(len(self.values[0])):
                        temp_row.append(other * self.values[i][j])  # multiply each element by number
                    result.append(temp_row)  # adds the rows of the result to the matrix
                    temp_row = []
                scalar_result = Matrix(len(result), len(result[0]), result)
                return scalar_result
            else:
                if len(self.values[0]) == len(other):  # matrix multiplication
                    result_matrix = []
                    t = 0
                    result_row = []
                    for i in range(len(self.values)):
                        while len(result_matrix) != len(self.values):
                            temp_value = 0
                            k = 0
                            for j in self.values[i]:
                                temp_value += j * other.values[k][t]  # calculation of the element of the result
                                k += 1
                            result_row.append(temp_value)  # adds the element of the row of the result
                            t += 1
                            if len(result_row) == len(other.values[0]):
                                result_matrix.append(result_row)  # adds the rows of the result to the matrix
                                result_row = []
                                t = 0
                                break
                    mul_matrix = Matrix(len(result_matrix), len(result_matrix[0]), result_matrix)
                    return mul_matrix
                else:
                    raise Exception(
                        f"Number of columns in first must be equal to number of rows in second.\nFirst: {self.m}x{self.n} Second: {len(other)}x{len(other.values[0])}")
        else:
            raise Exception(f"Unsupported operand type(s) for: '{self.__class__}' and '{other.__class__}'")

    @staticmethod
    def index_elem(sequence, start=0): # alternative way of enumerate function
        n = start
        for elem in sequence:
            yield n, elem
            n += 1

    def determinant(self):
        temp = 0
        if type(self) is Matrix:
            if len(self.values) == len(self.values[0]):  # checking if the matrix is square
                if len(self.values) == 1:  # 1 x 1 matrices
                    return self.values[0][0]  # determinant calculation
                else:
                    for e in range(len(self.values)):
                        temp += (-1) ** e * self.values[0][e] * Matrix.determinant(
                            [[item for loc, item in Matrix.index_elem(k) if loc != e] for k in
                             self.values[1:]])  # Used recursion and determinant rules
                    return temp
            else:
                raise Exception(
                    f"Matrix must be square for determinant calculation. Dimensions: {len(self.values)}x{len(self.values[0])}")
        else:
            if len(self) == len(self[0]):
                if len(self) == 1:  # 1 x 1 matrices
                    return self[0][0]  # determinant calculation
                else:
                    for e in range(len(self)):
                        temp += (-1) ** e * self[0][e] * Matrix.determinant(
                            [[item for loc, item in Matrix.index_elem(k) if loc != e] for k in
                             self[1:]])  # Used recursion and determinant rules
                    return temp
            else:
                raise Exception(
                    f"Matrix must be square for determinant calculation. Dimensions: {len(self)}x{len(self[0])}")

    def submatrix(self, a, b):
        if 0 <= a < self.m and self.n > b >= 0:  # check dimensions of the submatrix
            result_matrix = []
            for i in range(a):  # row of the submatrix
                result_row = []
                for j in range(b):  # column of the submatrix
                    result_row.append(self.values[i][j])  # adds the element of the row of the result
                result_matrix.append(result_row)  # adds the rows of the result to the matrix
            sub_matrix = Matrix(a, b, result_matrix)
            return sub_matrix.__str__()
        else:
            raise Exception(f"row and column numbers must be positive and smaller than dimension: {self.m}x{self.n}")


if __name__ == "__main__":
    try:
        print("Matrix(0, -1)")
        print(Matrix(0, -1))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, -1)")
        print(Matrix(2, 3, -1))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[3, 2])")
        print(Matrix(2, 3, values=[3, 2]))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[[9, 7.0, 4], 3.5])")
        print(Matrix(2, 3, values=[[9, 7.0, 4], 3.5]))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[[9, 7.0, 4], [3.5, -1, 2], [3, 6.5, 8]])")
        print(Matrix(2, 3, values=[[9, 7.0, 4], [3.5, -1, 2], [3, 6.5, 8]]))
    except Exception as error:
        print(error)

    try:
        print("Matrix(2, 3, values=[[9, 7.0, 4], [3.5, 2]])")
        print(Matrix(2, 3, values=[[9, 7.0, 4], [3.5, 2]]))
    except Exception as error:
        print(error)

    m1 = Matrix(4, 2, values=[[1, 2.0], [3, 2], [12, 6], [1, 0]])
    print("m1:", m1)
    m2 = Matrix(2, 4, values=[[1, 25, 4.5, 24.3368], [13.5, 82.2, 76, 13]])
    print("m2:", m2)
    m3 = Matrix(4, 4, values=[[1, 2.0, 3, 7], [3, 4, 5, 2], [9, 12, 15, 18], [1, 0, 1, 0]])
    print("m3:", m3)
    m4 = Matrix(2, 3, values=[[9, 7.0, 4], [3.5, 2, 6]])
    print("m4:", m4)
    m5 = Matrix(2, 3, values=[[1, 12.66, 4.7985], [1, 0, 1]])
    print("m5:", m5)

    try:
        print("m1 + m2")
        print(m1 + m2)
    except Exception as error:
        print(error)
    try:
        print("m1 - m2")
        print(m1 - m2)
    except Exception as error:
        print(error)
    try:
        print("m1 * m2")
        print(m1 * m2)
    except Exception as error:
        print(error)
    try:
        print("m1 * 2.5")
        print(m1 * 2.5)
    except Exception as error:
        print(error)
    try:
        print("m1 * \"2.5\"")
        print(m1 * "2.5")
    except Exception as error:
        print(error)
    try:
        print("m1 * m2 + m3")
        print(m1 * m2 + m3)
    except Exception as error:
        print(error)
    try:
        print("m4 + m5")
        print(m4 + m5)
    except Exception as error:
        print(error)
    try:
        print("m4 - m5")
        print(m4 - m5)
    except Exception as error:
        print(error)
    try:
        print("m4 * m5")
        print(m4 * m5)
    except Exception as error:
        print(error)

    print("m1.transpose()")
    print(m1.transpose())

    try:
        print("m1.submatrix(4, 1)")
        print(m1.submatrix(4, 1))
    except Exception as error:
        print(error)
    try:
        print("m1.submatrix(3, 1)")
        print(m1.submatrix(3, 1))
    except Exception as error:
        print(error)
    try:
        print("m2.determinant()")
        print(m2.determinant())
    except Exception as error:
        print(error)
    try:
        print("m3.determinant()")
        print(m3.determinant())
    except Exception as error:
        print(error)

    try:
        m6 = Matrix(4, 2)
        print("m6:", m6)
        m7 = Matrix(2, 4)
        print("m7:", m7)
        m8 = Matrix(4, 4)
        print("m8:", m8)
        m9 = Matrix(2, 3)
        print("m9:", m9)
        m10 = Matrix(2, 3)
        print("m10:", m10)

        try:
            print("m6 + m7")
            print(m6 + m7)
        except Exception as error:
            print(error)
        try:
            print("m6 - m7")
            print(m6 - m7)
        except Exception as error:
            print(error)
        try:
            print("m6 * m7")
            print(m6 * m7)
        except Exception as error:
            print(error)
        try:
            print("m6 * 2.5")
            print(m6 * 2.5)
        except Exception as error:
            print(error)
        try:
            print("m6 * \"2.5\"")
            print(m6 * "2.5")
        except Exception as error:
            print(error)
        try:
            print("m6 * m7 + m8")
            print(m6 * m7 + m8)
        except Exception as error:
            print(error)
        try:
            print("m9 + m10")
            print(m9 + m10)
        except Exception as error:
            print(error)
        try:
            print("m9 - m10")
            print(m9 - m10)
        except Exception as error:
            print(error)
        try:
            print("m9 * m10")
            print(m9 * m10)
        except Exception as error:
            print(error)

        print("m6.transpose()")
        print(m6.transpose())

        try:
            print("m6.submatrix(4, 1)")
            print(m6.submatrix(4, 1))
        except Exception as error:
            print(error)
        try:
            print("m6.submatrix(3, 1)")
            print(m6.submatrix(3, 1))
        except Exception as error:
            print(error)
        try:
            print("m7.determinant()")
            print(m7.determinant())
        except Exception as error:
            print(error)
        try:
            print("m8.determinant()")
            print(m8.determinant())
        except Exception as error:
            print(error)
    except Exception as error:
        print(error)
#sample input:
#1 2
#3 2
#12 6
#9 15
#1 0 0 0
#0 1 0 0
#3 5 6 6
#7 5
