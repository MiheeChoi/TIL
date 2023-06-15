n, m = map(int, input().split())
basket = [0]*n
for i in range(n):
    basket[i] = i+1

for _ in range(m):
    a, b = map(int, input().split())
    temp = basket[a-1]
    basket[a-1] = basket[b-1]
    basket[b-1] = temp

for j in range(len(basket)):
    print(basket[j], end=' ')
