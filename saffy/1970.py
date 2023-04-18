t = int(input())
for i in range(1,t+1):
    price = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0]*8
    for j in range(len(money)):
        change = price // money[j]
        if change>=1:
            cnt[j] += change
        price = price - change*money[j]
    print('#{}'.format(i))
    for h in range(len(cnt)):
        print('{}'.format(cnt[h]), end=' ')
    print('')
    # print('{} {} {} {} {} {} {} {}'.format(cnt[0],cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], cnt[6], cnt[7]))