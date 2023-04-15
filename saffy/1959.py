T = int(input())
for testcase in range(1,T+1):
    n,m = map(int,input().split())
    total = -float('inf')
    if n<=m:
        short = n
        long = m
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
    else:
        long = n
        short = m
        b = list(map(int,input().split()))
        a = list(map(int,input().split()))
    for i in range(long-short+1):
        max = 0
        for j in range(short):
            max += a[j]*b[i+j]
        if total<=max:
            total=max
    print('#{} {}'.format(testcase,total))
    