t = int(input())
for tc in range(1, t+1):
    num = int(input())
    arr = list(map(int, input().split()))
    winner = []
    cnt = 0
    for i in range(0, len(arr), 2):
        if arr[i] < arr[i+1]:
            winner.append(max(arr[i], arr[i+1]))
            cnt += arr[i+1] - arr[i]
        else:
            winner.append(max(arr[i], arr[i+1]))
            cnt += arr[i] - arr[i+1]
    print('#{} {}'.format(tc, cnt))
    print('{}'.format(winner))
