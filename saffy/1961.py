t = int(input())
for testcase in range(1,t+1):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(num)]

    #배열 0으로 초기화
    arr_90 = [[0 for _ in range(num)] for _ in range(num)]
    arr_180 = [[0 for _ in range(num)] for _ in range(num)]
    arr_270 = [[0 for _ in range(num)] for _ in range(num)]

    #arr 행렬 90도 회전
    for i in range(num):
        for j in range(num):
            arr_90[i][j] = arr[num-1-j][i]

    #arr90 행렬 90도 회전 -> arr180
    for i in range(num):
        for j in range(num):
            arr_180[i][j] = arr_90[num-1-j][i]

    #arr180 행렬 90도 회전 -> arr270
    for i in range(num):
        for j in range(num):
            arr_270[i][j] = arr_180[num-1-j][i]

    print('#{}'.format(testcase))
    for i in range(num):
        for a in range(num):
            print(arr_90[i][a],end='')
        print(end=' ')
        for b in range(num):
            print(arr_180[i][b],end='')
        print(end=' ')
        for c in range(num):
            print(arr_270[i][c],end='')
        print()
    
        
