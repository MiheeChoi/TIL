total = int(input())

numList = list(map(int,input().split()))
numList.sort()
midNum = int(total/2)
print(numList[midNum])