time, minutes = map(int, input().split())
minutes -= 45
if minutes < 0:
    minutes += 60
    time -= 1
if time < 0:
    time += 24
print(time, minutes)
