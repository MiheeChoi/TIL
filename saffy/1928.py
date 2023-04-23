# decodeAZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# decode = {i:ord(i)-65 for i in decodeAZ}
# for a in decodeAZ.lower():
#     decode[a] = ord(a)-71
t = int(input())
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]

for testcase in range(1,t+1):
    word = list(input())
    for i in range(len(word)):
        #word -> 표 숫자
        num = decode.index(word[i])
        #num을 이진수로


