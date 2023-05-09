for testcase in range(10):
    case = int(input())
    numlist = list(map(int, input().split()))
    while numlist[-1] != 0:
        for i in range(1, 6):
            numlist.append(numlist.pop(0) - i)
            if numlist[-1] <= 0:
                numlist[-1] = 0
                break
    print('#{}'.format(testcase+1), end=' ')
    for j in range(len(numlist)):
        print('{}'.format(numlist[j]), end=' ')
