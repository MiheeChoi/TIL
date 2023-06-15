numlist = [0] * 10
for i in range(10):
    num = int(input())
    numlist[i] = num % 42
set_numlist = set(numlist)
print(len(set_numlist))
