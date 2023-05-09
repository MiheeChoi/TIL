t = 10
for testcase in range(1, t+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for j in range(n):
        r, c = 0, j
        stack = []
        while r < n:
            if not stack and a[r][c] == 1:
                stack.append(1)
            elif stack and a[r][c] == 2:
                cnt += stack.pop()
            r += 1
    print('#{} {}'.format(testcase, cnt))
