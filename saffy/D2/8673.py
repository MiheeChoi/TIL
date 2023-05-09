import math
t = int(input())
for tc in range(1, t+1):
    num = int(input())
    arr = list(map(int, input().split()))
    winner = []
    cnt = 0
    total_game = math.sqrt(num)
    for i in range(0, len(arr), 2):
        if arr[i] < arr[i+1]:
            winner.append(max(arr[i], arr[i+1]))
            cnt += arr[i+1] - arr[i]
        else:
            winner.append(max(arr[i], arr[i+1]))
            cnt += arr[i] - arr[i+1]

    for j in range(0, total_game-1, 1):
        second_winner = []
        for k in range(0, len(winner), 2):
            if winner[k] < winner[k+1]:
                second_winner.append(max(arr[i], arr[i+1]))
                cnt += arr[i+1] - arr[i]
            else:
                winner.append(max(arr[i], arr[i+1]))
                cnt += arr[i] - arr[i+1]

    print('#{} {}'.format(tc, cnt))
    print('{}'.format(winner))
