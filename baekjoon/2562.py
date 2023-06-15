numlist = [i for i in range(9)]
for i in range(9):
    num = int(input())
    numlist[i] = num
print(max(numlist))
print(numlist.index(max(numlist)))
