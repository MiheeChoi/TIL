t = int(input())
for testcase in range(1,t+1):
    input_num = int(input())
    numbers = [2,3,5,7,11]
    result = []
    for number in numbers:
        cnt = 0
        while True:
            if input_num % number == 0:
                input_num = input_num/number
                cnt +=1
            else:
                result.append(str(cnt))
                break
    print('#{} {}'.format(testcase,' '.join(result)))
