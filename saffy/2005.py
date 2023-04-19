# t = int(input())
# for testcase in range(1,t+1):
#     n = int(input())
#     a = list(range(len(n))) #[0,1,2,3,4,...]
#     each = 0
#     for i in range(num):
#         if a[i] == a[0] or a[i]==a[i]:
#             print('{}'.format(1))
TC = int(input())

for t in range(1, TC+1):
    result = []
    n = int(input())
    for i in range(n):
        temp = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(result[i-1][j] + result[i-1][j-1])
        result.append(temp)

    print('#%d' % t)
    for i in result:
        print(*i)
