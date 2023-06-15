num = int(input())
num_arr = list(map(int, input().split()))
cnt = 0
target_num = int(input())
for i in range(num):
    if num_arr[i] == target_num:
        cnt += 1
print(cnt)
