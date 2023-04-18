t = int(input())
grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
for testcase in range(1,t+1):
    totalNum, targetNum = map(int,input().split())
    totalScoreList = [0]*totalNum
    for i in range(totalNum):
        mid, final, assi = map(int, input().split())
        totalScoreList[i] = mid*0.35 + final*0.45 + assi*0.2
    targetScore = totalScoreList[targetNum-1]
    totalScoreList.sort(reverse=True)
    div = totalNum//10
    final_target_score = totalScoreList.index(targetScore) // div
    print('#{} {}'.format(testcase,grades[final_target_score]))

