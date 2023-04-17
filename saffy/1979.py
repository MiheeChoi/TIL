t = int(input())
for testcase in range(1,t+1):
    n,k = list(map(int,input().split()))
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    #행
    for i in range(n):
        cnt=0
        for j in range(n):
            if puzzle[i][j] == 1:
                cnt +=1
            if puzzle[i][j] == 0 or j==n-1:
                if cnt == k:
                    ans +=1
                if puzzle[i][j] == 0:
                    cnt=0
    #열
    for i in range(n):
        cnt = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                cnt +=1
            if puzzle[j][i] == 0 or j == n-1:
                if cnt == k:
                    ans +=1
                if puzzle[j][i] == 0:
                    cnt = 0
    print('#{} {}'.format(testcase,ans))

