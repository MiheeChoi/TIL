t = 10
for tc in range(1, t+1):
    n, password = input().split()
    n = int(n)
    password = list(password)
    i = 0
    while (True):
        if password[i] == password[i+1]:
            del (password[i:i+2])
            n = n-2
            i = i-2
        i += 1
        if i == n-1:
            break

    print('#{}'.format(tc), end=' ')
    for j in range(len(password)):
        print('{}'.format(password[j]), end='')
    print()
