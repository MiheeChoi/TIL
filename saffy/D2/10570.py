t = int(input())
for tc in range(1,t+1):
    a, b = map(int, input().split())
    cnt = 0
    for i in range(a,b+1):
        c = i ** (1/2)
        if c == int(c):
            i = str(i)
            c = str(int(c))
            if i == i[::-1] and c == c[::-1]:
                cnt +=1
    print('#{} {}'.format(tc,cnt))