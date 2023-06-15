num = int(input())
score_arr = list(map(int, input().split()))
max_score = max(score_arr)
for i in range(num):
    score_arr[i] = score_arr[i]/max_score*100
total_sum = sum(score_arr)
print(total_sum/num)
