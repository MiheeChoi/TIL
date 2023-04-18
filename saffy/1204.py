t = int(input())
for testcase in range(1,t+1):
    order = int(input())
    grades = list(map(int,input().split()))
    cntList = [0] * 101
    mostNum = 0 #최빈값
    for grade in grades:
        cntList[grade] += 1
        if cntList[grade] >=cntList[mostNum]:
            mostNum = grade
    print('#{} {}'.format(testcase,mostNum))