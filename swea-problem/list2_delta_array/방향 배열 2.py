# 2차원 배열을 다음과 같이 하드코딩 해 주세요.

# 좌표 y=0 이고, x=1 일때, 상, 하, 좌, 우의 합을 구해 보세요.
# [출력]
# 선택한 지점을 기준으로 상, 하, 좌, 우의 합계(sum_v)

arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

y, x = 0, 1

sum_v = 0

for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]

    if ny < 0 or nx < 0:
        continue

    sum_v += arr[ny][nx]

print(sum_v)

# ------------- 강사님 풀이 ---------------------

arr = [
    [1, 2, 1, 3, 1],
    [2, 2, 2, 2, 2],
    [1, 0, 1, 0, 1],
    [3, 1, 2, 1, 3]
]

y = 0
x = 1

# 상 하 우 좌
# d : dirrection, delta
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

sum_v = 0
# 코드 4줄 암기!!
for i in range(4): # 방향은 4방향이라서(상하좌우)
    ny = y + dy[i] # n : new, next
    nx = x + dx[i]

    # 단점 : 들여쓰기가 하나 늘었다.
    # if 0 <= ny < 4 and 0 <= nx < 5: # 범위 체크
    #     sum_v += arr[ny][nx]

    # continue
    if ny < 0 or nx < 0 or ny >= 4 or nx >= 5: continue
    sum_v += arr[ny][nx]

print(sum_v)
