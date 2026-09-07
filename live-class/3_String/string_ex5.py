# 첫 줄에 N, 다음에 NxN 미로. 0 통로, 1 벽, # 로봇. 상하좌우로 모두 이동할 수 있는 칸 수는?

N = int(input())
text = [input() for _ in range(N)]

# 델타 사용
ans = 0     # 4 방향이 모두 통로인 칸 수

for i in range(N):
    for j in range(N):
        if text[i][j] != '1':    # 벽이 아니면
            cnt = 0     # 현재 위치에서 주변의 통로 개수
            for di, dj in [[0,1], [1, 0], [0, -1], [-1, 0]]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if text[ni][nj] != '1':
                        cnt += 1
            if cnt == 4:
                ans += 1

print(ans)
