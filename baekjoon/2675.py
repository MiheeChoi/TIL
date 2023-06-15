num = int(input())
stringlist = [0] * num
numlist = [0] * num
for i in range(num):
    input_num, input_str = input().split()
    input_num = int(input_num)
    stringlist[i] = input_str
    numlist[i] = input_num
    for j in range(len(input_str)):
        for k in range(input_num):
            print(input_str[j], end='')
    print()
