t = int(input())

for testcase in range(1,t+1):
    month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    m1, d1, m2, d2 = map(int, input().split())
    answer = 0
    for i in range(m1,m2):
        if m1 == i:
            answer += month[i] - d1 +1
        else:
            answer += month[i]
    answer += d2
    print('#{} {}'.format(testcase,answer))

    