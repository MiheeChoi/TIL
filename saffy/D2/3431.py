t = int(input())
for testcase in range(1,t+1):
    L,U,X = map(int,input().split())
    if X>=U:
        result = -1
    elif L<=X and X<=U:
        result = 0
    elif X<L:
        result = L-X
    print('#{} {}'.format(testcase,result))