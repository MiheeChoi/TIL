t = int(input())
for tc in range(1, t+1):
    arr = list(map(int, input().split()))
    sum_arr = []
    for i in range(10):
        sum_arr.append(sum(list(map(int, str(arr[i])))))
    print('#{} {} {}'.format(tc, max(sum_arr), min(sum_arr)))
