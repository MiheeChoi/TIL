T = int(input())
for x in range(1,T+1):
    num=int(input())
    count = 0
    zero_to_nine = [str(i) for i in range(10)]
    while zero_to_nine:
        count +=1
        total = num * count
        total = str(total)
        for j in total:
            if j in zero_to_nine:
                zero_to_nine.remove(j)
    print('#{} {}'.format(x,total))