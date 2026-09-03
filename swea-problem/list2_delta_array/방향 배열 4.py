# 2차원 배열을 다음과 같이 하드코딩 해 주세요.

# y, x 좌표를 입력받고, 오른쪽, 왼쪽, 아래, 오른쪽 아래 대각선의 최대값을 구해 보세요.
# [입력]
# 두 정수를 입력받습니다.
# [출력]
# 선택한 지점을 기준으로 오른쪽, 왼쪽, 아래, 오른쪽 아래 대각선 값의 최대값(max_v)

arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

dy = [0, 0, 1, 1]
dx = [1, -1, 0, 1]

y, x = map(int, input().split())

max_v = float('-inf')

for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]

    if ny < 0 or nx < 0 or ny >= len(arr) or nx >= len(arr[0]):
        continue

    if max_v < arr[ny][nx]:
        max_v = arr[ny][nx]

print(max_v)

# ------------- 강사님 풀이 ---------------------
y, x = map(int, input().split())

arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]
# 하, 우, 좌, 우하
dy = [1, 0, 0, 1]
dx = [0, 1, -1, 1]

max_v = float('-inf') # 음의 무한대

for i in range(4): # 방향은 4방향
    ny = y + dy[i]
    nx = x + dx[i]

    if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
    # 최대값 갱신 코드
    if arr[ny][nx] > max_v : max_v = arr[ny][nx]

print(max_v)
