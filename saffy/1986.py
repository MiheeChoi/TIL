times = int(input())

for i in range(1,times+1):
    num = int(input())
    sum = 0
    for j in range(1,num+1):
        if j%2==0:
            sum -=j
        else:
            sum +=j
    print('#%d %d' % (i,sum))
    

    