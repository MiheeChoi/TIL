t = int(input())
vowel = ['a','e','i','o','u']
for tc in range(1,t+1):
    arr = list(input())
    for i in range(len(arr)):
        for j in vowel:
            if j in arr:
                arr.remove(j)
    print('#{}'.format(tc),end=' ')
    for b in range(len(arr)):
        print('{}'.format(arr[b]), end='')
    print()

    
