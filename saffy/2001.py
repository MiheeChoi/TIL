t = int(input())
for testcase in range(1,t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(n)]
    max = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum=0
            for x in range(i, m+i):
                for y in range(j,m+j):
                    sum += arr[x][y]
                
            if max<sum:
                max = sum
    print('#{} {}'.format(testcase,max))
