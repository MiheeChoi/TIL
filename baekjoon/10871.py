a, b = map(int, input().split())
num_arr = list(map(int, input().split()))
cnt = 0
for i in range(a):
    if num_arr[i] < b:
        print(num_arr[i], end=' ')
