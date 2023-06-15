student_list = [0] * 31
for i in range(28):
    student = int(input())
    student_list[student] = 1
print(student_list)
for j in range(1, len(student_list)):
    if student_list[j] == 0:
        print(j)
print(student_list)
