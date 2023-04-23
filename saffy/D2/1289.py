t = int(input())
for testcase in range(1,t+1):
    aim = list(input())
    zero = ['0'] * len(aim)
    cnt = 0
    for i in range(len(aim)):
        if aim[i] != zero[i]:
            zero[i:] = aim[i]*len(zero[i:])
            cnt +=1
    print('#{} {}'.format(testcase,cnt))