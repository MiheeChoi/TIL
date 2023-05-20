t = 10
for tc in range(1, t+1):
    n = int(input())
    buildings = list(map(int, input().split()))
    count = 0
    others = [-2, -1, 1, 2]
    for i in range(2, n-2):
        # 양 쪽 옆 빌딩들의 높이 배열
        side = []
        for j in others:
            side.append(buildings[i+j])
        if max(side) > buildings[i]:
            continue
        # 양쪽의 건물중 제일 높은것이 i번째 빌딩보다 높으면 -> 카운트 안됨 continue
        count += buildings[i] - max(side)
        # 카운트에는 i번째 빌딩에서 옆 빌딩들 배열중 제일 큰 것을 뺀 걸 더해
    print('#{} {}'.format(tc, count))
