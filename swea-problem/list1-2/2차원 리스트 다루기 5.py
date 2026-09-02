# 2차원 리스트를 다음과 같이 하드코딩 해 주세요.
# 다음 2차원 리스트를 그림과 같이 열순회 하여 출력해 주세요
# [출력]
# 첫 번째 열부터 마지막 열까지 순서대로 출력

arr = [
    [5, 4, 2, 1],
    [3, 7, 7, 7],
    [2, 2, 1, 1]
]

for j in range(4):
    for i in range(3):
        print(arr[i][j], end=' ')
    print()

# 강사님 풀이
for x in range(4):
    for y in range(3):  # 열 고정하고 y부터
        print(arr[y][x], end=' ')
    print()