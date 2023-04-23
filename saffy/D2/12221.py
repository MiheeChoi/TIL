t = int(input())
for tc in range(1,t+1):
    a,b = map(int, input().split())
    result = 0
    if a>=10 or b>=10:
        result = -1
    else:
        result = a*b
    print('#{} {}'.format(tc,result))