t = int(input())
for testcase in range(1,t+1):
    arr = input()
    cnt =0
    answer = 0
    for j in range(1, 10):
        if arr[0] != arr[j] or arr[1] != arr[j+1]:
            cnt +=1
        else:
            break
    answer=cnt+1
    print('#{} {}'.format(testcase,answer))