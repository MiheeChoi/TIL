t = int(input())
for tc in range(1,t+1):
    people = int(input())
    result = [0]*people
    print('#{}'.format(tc),end=' ')
    for i in range(people):
        print('{}{}{}'.format(1,'/',people), end=' ')
    print()