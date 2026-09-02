# 1. 4 x 4 2차원 리스트를 입력받아 주세요.
# 2. 그 리스트를 거꾸로 출력해 보세요
# [입력]
# 4행 4열 2차원 리스트를 입력받습니다.
# [출력]
# 거꾸로 순회하여 출력합니다.

arr = [list(map(int, input().split())) for _ in range(4)]

for i in range(3, -1, -1):
    for j in range(3, -1, -1):
        print(arr[i][j], end=' ')
    print()

# 강사님 풀이
arr = [list(map(int, input().split())) for _ in range(4)]

for y in range(3, -1, -1):  # 3부터 0까지 -1씩
    for x in range(3, -1, -1):
        print(arr[y][x], end=' ')
    print()
