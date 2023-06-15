n, m = map(int, input().split())
basket = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        basket[a] = k

for b in range(n):
    print(basket[b], end=' ')
