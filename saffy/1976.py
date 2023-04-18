t = int(input())
for i in range(1,t+1):
    t1, m1, t2, m2 = map(int, input().split())
    ans_h = t1+t2
    if t1 + t2 >=12:
        ans_h = (t1+t2)-12
    ans_m = m1 + m2
    if m1+m2 >=60:
        ans_m = (m1+m2)-60
        ans_h +=1
    print('#{} {} {}'.format(i,ans_h,ans_m))
    