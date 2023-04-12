# num = int(input())

# for i in range(num):
#     numList = list(map(int,input().split()))
#     if numList[0]>numList[1]:
#         result = ">"
#     elif numList[0] == numList[1]:
#         result="="
#     else:
#         result="<"
#     print('#%d %s'%(i,result))

T = int(input())
for tt in range(0, T):
    a, b = map(int, input().split())
    print( f"#{tt+1} ", end='' )
    if a < b:
        print("<")
    elif a == b:
        print("=")
    else:
        print(">")