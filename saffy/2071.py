num = int(input())
total = 0
for i in range(num):
    numList = list(map(int, input().split()))
    total = sum(numList)
    result = total/len(numList)
    print('#%d %d'%(i,round(result)))
