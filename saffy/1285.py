t = int(input())
for testcase in range(1,t+1):
    people = int(input())
    distance = list(map(int,input().split()))

    for i in range(len(distance)):
        distance[i] = abs(distance[i])
    # for i in range(len(distance)):
    #     if distance[i]<0:
    #         distance[i] = -1 * distance[i]
    
    # distance.sort()
    # cnt = 0
    # for j in range(len(distance)):
    #     if distance[0] == distance[j]:
    #         cnt = cnt+1

    print('#{} {} {}'.format(testcase,min(distance),distance.count(min(distance))))

