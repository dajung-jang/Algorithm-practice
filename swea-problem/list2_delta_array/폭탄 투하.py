# 4 x 5 사이즈의 맵(문자 배열)을 준비합니다. 모든 칸의 값은 '_' (언더바)로 채워줍니다.
# 그리고 폭탄을 투하할 좌표(Y, X) 두 곳을 입력 받아주세요. 그리고 두 폭탄이 터진 후의 맵을 출력해 주세요.
# 폭탄이 터지면 상하좌우, 그리고 대각선 방향이 '#'으로 표시됩니다.
# [예시]
# 폭탄이 (1, 1), 그리고 (3, 3) 좌표에 투하되었다면,
# (1,1) 위치의 폭탄이 터지면 아래와 같이 맵이 변경됩니다.
# 다시 한번 (3,3)의 폭탄이 터지면 아래와 같이 맵이 변경됩니다.
# 입력
# 첫 줄에는 첫번째 폭탄을 투하 할 좌표 (Y, X) 를 입력 받습니다.
# 두 번째 줄에는 두 번째 폭탄을 투하 할 좌표 (Y, X)를 입력 받습니다.
# 출력
# 두 개의 폭탄이 터진 후 의 맵을 출력합니다.

arr = [list(['_'] * 5) for _ in range(4)]

Y, X = map(int, input().split())
y, x = map(int, input().split())

dy = [-1, 1, 0, 0, -1, -1, 1, 1]
dx = [0, 0, 1, -1, -1, 1, 1, -1]

for i in range(8):
    ny1 = Y + dy[i]
    nx1 = X + dx[i]
    ny2 = y + dy[i]
    nx2 = x + dx[i]

    if not (ny1 < 0 or nx1 < 0 or ny1 >= len(arr) or nx1 >= len(arr[0])):
        arr[ny1][nx1] = '#'

    if not (ny2 < 0 or nx2 < 0 or ny2 >= len(arr) or nx2 >= len(arr[0])):
        arr[ny2][nx2] = '#'

for i in range(4):
    print(*arr[i])

# ------------- 강사님 풀이 ---------------------

# 4행 5열
arr = [['_'] * 5 for _ in range(4)]

# 폭탄 좌표 2개 입력
for _ in range(2):
    y, x = map(int, input().split())
    # 상, 하, 좌, 우, 대각선
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(8): # 8방향
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
        arr[ny][nx] = '#' # 폭탄 터트리기

for row in arr: # row는 1차원 배열
    print(*row)
