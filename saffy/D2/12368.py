t = int(input())
for testcase in range(1,t+1):
    t1,t2 = map(int,input().split())
    result = (t1 + t2) % 24
    if result == 24:
        result = 0
    print('#{} {}'.format(testcase,result))
   
