def read_grades(filename):
    file = open(filename, "r", encoding="utf-8")  # open file
    lines = file.readlines()  # read lines
    list_std = []
    for i in lines:
        k = i.rstrip()
        list_std.append(k.split(","))  # adding the lines to the list
    mt1_dict = {}
    mt2_dict = {}
    final_dict = {}
    name_dict = {}
    for i in range(len(list_std)):
        name_dict[list_std[i][0]] = list_std[i][1]  # Key=StudentNo ,Value=Name

    for i in range(len(list_std)):
        if list_std[i][2] == "midterm1":  # checking the exam type
            mt1_dict[list_std[i][0]] = list_std[i][3]  # Key=StudentNo ,Value=Midterm1Score

        elif list_std[i][2] == "midterm2":  # checking the exam type
            mt2_dict[list_std[i][0]] = list_std[i][3]  # Key=StudentNo ,Value=Midterm2Score

        elif list_std[i][2] == "final":  # checking the exam type
            final_dict[list_std[i][0]] = list_std[i][3]  # Key=StudentNo ,Value=FinalScore

        else:
            pass

    name, mt1, mt2, final = name_dict, mt1_dict, mt2_dict, final_dict  # matching the name,mt1,mt2,and final with the dictionaries

    return name, mt1, mt2, final


def convert(names, midterm1, midterm2, final):
    lst = []
    for key in names.keys():
        lst.append((key, names[key], midterm1[key], midterm2[key],
                    final[key]))  # a set is created for each student and added to the list
    return lst


def calculate_exam_average(lst, exam):
    sum_of_list = 0
    average = 0.0
    for i in lst:
        if exam == "midterm1":  # checking the exam type
            sum_of_list += int(i[2])  # adding the midterm 1 scores to the total score
        elif exam == "midterm2":  # checking the exam type
            sum_of_list += int(i[3])  # adding the midterm 2 scores to the total score
        elif exam == "final":  # checking the exam type
            sum_of_list += int(i[4])  # adding the final scores to the total score
        else:
            pass
    if len(lst) != 0:  # To avoid the zero division error
        average = sum_of_list / len(lst)  # total score/number of students to find average score
    else:
        pass
    return average


def find_passing_students(lst):
    student_names = []
    for i in lst:
        if int(i[2]) * 0.3 + int(i[3]) * 0.3 + int(
                i[4]) * 0.4 > 60:  # calculate students's overall scores and check if they pass
            student_names.append(i[1])  # if the student passes,add to the list
    return student_names


def manipulate(filename, lst):
    file2 = open(filename, "r", encoding="utf-8")  # open file
    lines2 = file2.readlines()  # read lines
    list_std2 = []
    list_new = []
    for i in lst:  # sets are immutable so I add the elements of lst to a new list
        list_new.append(list(i))
    for i in lines2:
        k = i.rstrip()
        list_std2.append(k.split(","))  # adding the lines of the file to the list
    for u in list_std2:
        t = 0
        if list_new[t][0] != u[0]:  # finding common students of the lists and manipulating exam scores
            while t < len(list_new) - 1:
                t += 1
                if list_new[t][0] == u[0]:
                    if u[1] == "midterm1":  # checking the exam type
                        list_new[t][2] = u[2]  # changing the midterm 1 score
                    elif u[1] == "midterm2":  # checking the exam type
                        list_new[t][3] = u[2]  # changing the midterm 2 score
                    elif u[1] == "final":  # checking the exam type
                        list_new[t][4] = u[2]  # changing the final score
                    else:
                        pass
                    break
    result = list_new
    return result


def write_grades(filename, lst):
    file = open(filename, "w")  # open file
    file.write("ID,Name,Midterm 1,Midterm 2,Final" + "\n")  # write on the first line
    for i in lst:
        file.write(str(
            i[0] + "," + i[1] + "," + i[2] + "," + i[3] + "," + i[4]) + "\n")  # write each element of the list in lines
    file.close()


if __name__ == '__main__':
    names, midterm1, midterm2, final = read_grades("grades.csv")
    lst = convert(names, midterm1, midterm2, final)
    print(lst)
    print("midterm1: ", calculate_exam_average(lst, "midterm1"))
    print("midterm2: ", calculate_exam_average(lst, "midterm2"))
    print("final: ", calculate_exam_average(lst, "final"))
    print(find_passing_students(lst))
    lst = manipulate("edit.csv", lst)
    print("midterm1: ", calculate_exam_average(lst, "midterm1"))
    print("midterm2: ", calculate_exam_average(lst, "midterm2"))
    print("final: ", calculate_exam_average(lst, "final"))
    print(find_passing_students(lst))
    write_grades("cumulative.csv", lst)
