str1 = list(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in str1:
        print(str1.index(i), end=' ')
    else:
        print(-1, end=' ')
