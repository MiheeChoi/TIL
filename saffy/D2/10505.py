t =int(input())
for testcase in range(1,t+1):
    num = int(input())
    num_list= list(map(int,input().split()))
    sum = 0
    for a in range(num):
        sum += num_list[a]
    avg = int(sum/num)
    cnt = 0
    for i in range(num):
        if num_list[i] <= avg:
            cnt +=1
    print('#{} {}'.format(testcase,cnt))