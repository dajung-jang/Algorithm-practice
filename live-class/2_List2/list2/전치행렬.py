
# i : 행의 좌표, 행의 크기 len(arr)
# j : 열의 좌표, 열의 크기 len(arr[0])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3X3 행렬

for i in range(3):
    for j in range(3):  # for j in range(i):인 경우
        if i < j:       # if 문 필요 없음
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


