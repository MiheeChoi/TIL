t = int(input())
for testcase in range(1,t+1):
    n = int(input())
    result = []
    for i in range(n):
        temp=[]
        for j in range(i+1):
            if j==0 or j==i:
                temp.append(1)
            else:
                temp.append(result[i-1][j-1]+result[i-1][j])
        result.append(temp)
    print('#{}'.format(testcase))
    for i in result:
        print(*i)
        ## *i는 각 리스트 띄어쓰기 


