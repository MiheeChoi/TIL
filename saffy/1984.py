import math

t = int(input())
for testcase in range(1,t+1):
    numlist = list(map(int,input().split()))
    numlist.sort()
    sum = 0
    for i in range(1,9):
        sum +=numlist[i]
    avg = round(sum/8)
    print('#{} {}'.format(testcase, avg))