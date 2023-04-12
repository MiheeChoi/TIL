t = int(input())

for i in range(1,t+1):
    data = list(map(int, input().split()))
    data.sort()
    maxNum = data[-1]
    print("#{} {}".format(i,maxNum))


