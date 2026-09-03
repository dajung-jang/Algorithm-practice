# 배열을 다음과 같이 하드코딩 해 주세요.
# 배열의 각 element의 범위는 1부터 30까지 입니다.
# 정수 n을 입력받고, n이 배열 arr에 몇개 있는지 출력해 보세요.
# 반드시, dat배열을 활용해 주세요.
# [입력]
# 정수 한개를 입력받습니다.
# [출력]
# 갯수를 출력합니다.

arr = [
    [1, 5, 10, 15],
    [15, 15, 20, 30]
]

dat = [0] * 31  # 인덱스를 0부터 30까지 쓸거니까
idx = 0

for i in range(2):
    for j in range(4):
        idx = arr[i][j]
        dat[idx] += 1

n = int(input())
print(dat[n])

# ------------- 강사님 풀이 ---------------------

arr = [
    [1, 5, 10, 15],
    [15, 15, 20, 30]
]

dat = [0] * 31 # 인덱스를 0부터 30까지 쓸거니까

for y in range(2): # 2행
    for x in range(4): # 4행
        idx = arr[y][x] # 값을 인덱스로
        dat[idx] += 1 # counting

n = int(input())
print(dat[n])