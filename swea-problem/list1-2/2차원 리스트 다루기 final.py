# 5 x 5 2차원 리스트를 입력받아 주세요.
# 1. 정수 2의 개수가 몇개인지 counting 후 출력
# 2. 가장 큰 값과 가장 작은 값 출력
# 3. 좌상단에서 우하단으로 내려가는 대각선 요소들 합계 출력
# <주의> 메서드 사용금지(count), 내장함수 사용금지(sum, max, min)
# [입력]
# 5행 5열 2차원 리스트를 입력받습니다.
# [출력]
# 1~3번 결과가 순서대로 출력됩니다.

arr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
min_v = float('inf')
max_v = float('-inf')
sum_v = 0

for i in range(5):
    for j in range(5):
        if arr[i][j] == 2: cnt += 1
        if arr[i][j] < min_v: min_v = arr[i][j]
        if arr[i][j] > max_v: max_v = arr[i][j]
    sum_v += arr[i][i]

print(cnt)
print(max_v, min_v)
print(sum_v)

# ----------------------------------------------------------
# 강사님 풀이

# 리스트 컴프리헨션 무조건 써라
arr = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
sum_v = 0
# 나는 행순회를 할거다!! (첫 좌표 값)
max_v = arr[0][0]
min_v = arr[0][0]

# 행순회
for y in range(5):
    for x in range(5):
        # 2의 개수를 counting
        if arr[y][x] == 2: cnt += 1
        # 최대값 갱신
        if arr[y][x] > max_v: max_v = arr[y][x]
        # 최소값 갱신
        if arr[y][x] < min_v: min_v = arr[y][x]
    # 대각선의 합
    sum_v += arr[y][y]

print(cnt)
print(max_v, min_v)
print(sum_v)