t = int(input())
for testcase in range(1,t+1):
    n = int(input())
    speed = 0
    move = 0
    for i in range(n):
        command = list(map(int,input().split()))
        if command[0] == 1:
            speed += command[1]
        elif command[0] == 2:
            if speed - command[1] >0:
                speed -=command[1]
            else:
                speed = 0
        else:
            move +=0
        move += speed
    print('#{} {}'.format(testcase,move))