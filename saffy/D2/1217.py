import math
#math로 풀기
# while True:
#     num = int(input())
#     result = 0
#     a,b =map(int,input().split())
#     result = int(math.pow(a,b))
#     print('#{} {}'.format(num,result))

#재귀함수
for _ in range(10):
    num = int(input())
    a,b =map(int,input().split())

    def pow(a,b):
        if b==0:
            return 1
        else:
            return a * pow(a,b-1)

    print('#{} {}'.format(num,pow(a,b)))


