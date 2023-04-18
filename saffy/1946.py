t = int(input())
for testcase in range(1,t+1):
    times = int(input())
    values = ''
    for i in range(times):
        c,k = input().split()
        values += c*int(k)
    print('#{}'.format(testcase))
    for j in range(0,len(values),10):
        print(values[j:j+10])
