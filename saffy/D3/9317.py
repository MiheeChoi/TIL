t = int(input())
for testcase in range(1, t+1):
    difference = 0
    length = int(input())
    arrlist = list(input())
    answer_list = list(input())
    for i in range(0, len(arrlist)):
        if arrlist[i] == answer_list[i]:
            difference = difference+1

    print('#{} {}'.format(testcase, difference))
