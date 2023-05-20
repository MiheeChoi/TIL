input_str = input().strip('[]')
#strip함수는 input에 []을 지워주는 함수이다. 그냥 input으로 받게되면, 스트링 하나로 인식하기 때문에 []있는 상태에서 split이 안됨.
arr = [int(x) for x in input_str.split(',')]
arrlen = len(arr)
rankarr = [0]*arrlen

for i in range(arrlen):
    rank = 1
    for j in range(arrlen):
        if arr[j]>arr[i]:
            rank +=1
    rankarr[i] = rank
print(rankarr)