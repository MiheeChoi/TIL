inputNum = int(input())

for i in range(1,inputNum+1):
    numList = list(map(int,input().split()))
    sum = 0
    for j in range(len(numList)):
        if numList[j]%2 == 1:
            sum +=numList[j]
    print('#%d %d' % (i,sum))

    