num = int(input())
for i in range(1,num+1):
    count = 0
    s = str(i)
    for x in s:
        if (x=='3') or (x=='6') or (x=='9'):
            count +=1
    if count == 0:
        print(i, end=' ')
    else:
        print(count*'-', end=' ')


    