t = int(input())
for testcase in range(1,t+1):
    result=0
    arr = [list(map(int,input().split())) for i in range(9)]
    cnt_1=0
    cnt_2=0
    cnt_3=0
    for m in range(9):
        comp_list = [0] * 9
        for n in range(9):
            comp_list.append(arr[m][n])
            comp_list.sort()
            if comp_list == [1,2,3,4,5,6,7,8,9]:
                cnt_1 +=1
                
            else:
                result=0
                break;
            print(cnt_1)
    
    for x in range(9):
        comp_list = [0]*9
        for y in range(9):
            comp_list.append(arr[y][x])
            comp_list.sort()
            if comp_list == [1,2,3,4,5,6,7,8,9]:
                x+=1
                cnt_1 +=1
            else:
                result = 0
                break;
    
    for a in range(0,9,3):
        for b in range(0,9,3):
            comp_list = [0] * 9
            for c in range(3):
                for d in range(3):
                    comp_list.append(arr[c][d])
                comp_list.sort()
                if comp_list == [1,2,3,4,5,6,7,8,9]:
                    cnt_3 +=1
                else:
                    result=0
                    
    if (cnt_1 == 9) and (cnt_2 == 9) and (cnt_3 == 9):
        result=1
    else:
        result=0

    print('#{} {}'.format(testcase,result))
    print('{} {} {}'.format(cnt_1,cnt_2,cnt_3))

       




t