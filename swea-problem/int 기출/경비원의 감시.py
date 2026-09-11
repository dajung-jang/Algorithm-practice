# N x N 크기의 격자 모양 건물이 있습니다. 이 건물의 각 칸은 빈 공간(0), 벽(1), 또는 경비원(2)으로 채워져 있습니다.
# 경비원은 정확히 1명만 존재하며, 자신이 있는 칸에서 상, 하, 좌, 우 네 방향으로 벽을 만나기 전까지 모든 칸을 감시할 수 있습니다.
# 당신의 임무는 이 단일 경비원이 감시하지 못하는 칸의 개수를 찾는 것입니다.
# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어집니다.
# 각 테스트 케이스의 첫 줄에는 건물의 크기 N이 주어집니다.
# 다음 N줄에 걸쳐 각 줄마다 N개의 숫자가 공백으로 구분되어 주어집니다.
# 0은 빈 공간, 1은 벽, 2는 경비원을 나타냅니다.
# [출력]
# 각 테스트 케이스마다 '#x'(x는 테스트케이스 번호)를 출력하고, 공백을 둔 다음 경비원이 감시하지 못하는 칸의 개수를 출력합니다.
# [제약사항]
# 1 ≤ N ≤ 100
# 벽은 1개 이상 존재할 수 있습니다.
# 경비원은 정확히 1명만 존재합니다.

def KFC(arr):
    dy = [-1, 1, 0, 0]  #상하좌우
    dx = [0, 0, -1, 1]

    global cnt
    cnt = 0

    # 먼저 상하좌우 한번씩 움직이고 그 다음 몇번 반복 ? -> 이것보단 똑같은 방향에서 몇번 갈지 반복하고 그 다음 방향으로 이동해야 벽 만났을 때 그 방향은 멈출수 있겠는데? -> 그 방향에서는 break
    for i in range(4):
        for j in range(1, N):
            ny = y + (dy[i] * j)
            nx = x + (dx[i] * j)
            if ny < 0 or ny >= N or nx < 0 or nx >= N: break
            elif arr[ny][nx] == 1: break
            cnt += 1
    return cnt

T = int(input())
for i in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 벽 개수
    m = 0
    # 경비원 위치 찾기
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 2:
                y = a
                x = b
            if arr[a][b] == 1: m += 1

    KFC(arr)

    result = (N * N) - m - cnt - 1  # 경비원 본인 위치빼줘야 해서 -1
    print(f'#{i} {result}')

