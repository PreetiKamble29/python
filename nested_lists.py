"""
Nested Lists
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
"""


if __name__ == '__main__':
    record_list = []
    score_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_list.append(score)
        record_list.append([name,score])
 
    sorted_score = list(sorted(set(score_list)))
    student_list = []
    for student, marks in record_list:
        if marks == sorted_score[1]:
            student_list.append(student)

    for student in sorted(student_list):
        print(student)
