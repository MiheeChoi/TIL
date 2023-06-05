total_price = int(input())
saving = 0
total_num = int(input())
for i in range(1, total_num+1):
    price, each = map(int, input().split())
    saving += price * each

if total_price == saving:
    print('Yes')
else:
    print('No')
