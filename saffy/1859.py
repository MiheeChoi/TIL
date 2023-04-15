T = int(input())
for i in range(1,T+1):
    day = int(input())
    numList = list(map(int,input().split()))[::-1]
    answer = 0
    maxNum = numList[0]
    for j in range(1,day):
        if maxNum>numList[j]:
            answer += maxNum-numList[j]
        else:
            maxNum = numList[j]
    print('#{} {}'.format(i,answer))
    