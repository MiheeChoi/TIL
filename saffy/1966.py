t = int(input())
for testcase in range(1, t+1):
    num = int(input())
    numlist = list(map(int, input().split()))
    numlist.sort()
    print('#{}'.format(testcase), end=' ')
    for i in range(num):
        print(numlist[i],end=' ')
    print()