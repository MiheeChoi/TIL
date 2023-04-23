t = int(input())
for testcase in range(1,t+1):
    student = int(input())
    team = int(student/3)
    print('#{} {}'.format(testcase,team))