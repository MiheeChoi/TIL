time, minutes = map(int, input().split())
cooking_time = int(input())

total_minutes = minutes + cooking_time

if (total_minutes > 60) or (total_minutes == 60):
    extra_time = total_minutes // 60
    total_minutes = total_minutes % 60
    time += extra_time


if time >= 24:
    time = time - 24

print(time, total_minutes)
