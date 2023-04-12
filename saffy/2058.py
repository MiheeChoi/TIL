n = input()
sum = 0
number = int(n)
for i in n:
    sum = sum + number%10
    number = (number - (number%10)) / 10
print(sum)
