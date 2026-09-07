# 첫 줄에 N, 다음에 NxN 지도, # 집중 호우 피해구역. 피해구역 수는?

N = int(input())
text = [input() for _ in range(N)]

count = 0

for i in range(N):
    for j in range(N):
        if text[i][j] == '#':
            count += 1

print(count)
