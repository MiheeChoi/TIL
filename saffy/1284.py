T = int(input())
for i in range(1,T+1):
    p, q, r, s, w = map(int, input().split())
    a_price = p*w
    if w<=r:
        b_price = q
    else:
        b_price = q + s*(w-r)

    cost = min(a_price,b_price)
    print('#{} {}'.format(i,cost))

    