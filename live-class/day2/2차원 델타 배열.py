# 델타를 활용한 2차원 배열 탐색
# 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
# 인덱스 (i, j)인 칸의 상하좌우 칸 (ni, nj)

# x방향은 j, y방향은 i 라고 생각하고 0, 1, -1 을 배정한다고 생각하면 됨
# di[] <- [0, 1, 0, -1]     # 방향별로 더할 값
# dj[] <- [1, 0, -1, 0]
#
# for k : 0 -> 3
#     ni <- i + dj[k]
#     nj <- j + dk[k]

# 코드 예시

# 방법 1

# arr[0...N-1][0...N-1]   # NXM 배열
# di[] <- [0, 1, 0, -1]
# dj[] <- [1, 0, -1, 0]
# for i : 0 -> N-1
#     for J : 0 -> N-1:
#         for d : 0 -> 3
#             ni <- i + di[d]
#             nj <- j + dj[d]
#             if 0 <= ni < N and 0 <= nj < N  # 유효한 인덱스면 => 모서리 4군데는 4면이 인접하지 않고 2면만 인접함 그래서 코드에서 오류 나기 때문에 그거 걸러주는것
#                 for(arr[ni][nj])

# 방법 2

# for i in range(N):
#     for j in range(N):
#         for di, df in [[0, 1], [1, 0],[0, -1], [-1,0]]:
#             ni, nj = i+di, j+dj
#             if ni의 범위

# 델타 응용
# ex) NxM 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최댓값 (k=2)

max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]  # i, j를 중심으로 (합계) 
        for di, dj in [[0, 1], [1, 0],[0, -1], [-1,0]]:     # 각 방향
            for c in range(1, k+1):                         # 거리별
                ni, nj = i+di*c, j+dj*c
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s