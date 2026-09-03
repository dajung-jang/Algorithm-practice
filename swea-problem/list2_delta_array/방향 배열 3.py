# 2차원 배열을 다음과 같이 하드코딩 해 주세요.

# y, x 좌표를 입력받고, 대각선 방향과 자기자신의 곱을 구해 보세요.
# [입력]
# 두 정수를 입력 받습니다.
# [출력]
# 선택한 지점을 기준으로 대각선 방향과 자기 자신의 곱을 출력 합니다.

arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

dy = [-1, -1, 1, 1]
dx = [-1, 1, 1, -1]

y, x = map(int, input().split())

# 자기자신이랑 곱해지게끔 초기 mul_v는 자기 자신으로 설정해놓기!
mul_v = arr[y][x]

for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]

    if ny < 0 or nx < 0 or ny >= len(arr) or nx >= len(arr[0]):
        continue

    mul_v *= arr[ny][nx]

print(mul_v)

# ------------- 강사님 풀이 ---------------------

y, x = map(int, input().split())

arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

# 현재위치, 대각선(좌상, 우상, 죄하, 우하)
dy = [0, -1, -1, 1, 1]
dx = [0, -1, 1, -1, 1]

gop_v = 1

for i in range(5): # 방향은 4방향 + 현재 위치
    ny = y + dy[i]
    nx = x + dx[i]

    if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
    gop_v *= arr[ny][nx]

print(gop_v)
