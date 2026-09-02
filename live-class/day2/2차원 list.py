# 입력
#3
#123
#456
#789
N = int(input())
# 숫자 하나하나 따로 구분해서 저장됨 줄띄움을 기준으로 저장됨(split()를 안쓴거임)
# arr 에 저장된 결과 : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = [list(map(int, input())) for _ in range(N)]
print(arr)

# -------------------------------------------------

# 0으로 채워진 3X4 배열 만들기
arr = [[0] * 4 for _ in range(3)]

# --------------------------------------------------
# 보통 행에는 i, 열에는 j를 많이 씀

# 배열 순회
# - n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
# - 행 우선 조회(가로)

# i 행의 좌표
# j 열의 좌표
# for i in range(n):
#     for j in range(m):
#         f(array[i][j])  # f 는 별 뜻 없고 함수를 의미함(print가 될수도 있고 필요한 함수를 작성하면 되는거임)

# --------------------------------------------------

# 열 우선 순회(세로)

# i 행의 좌표
# j 열의 좌표

# for j in range(m):
#     for i in range(n):
#         f(arr[i][j])

# --------------------------------------------------

# 행 우선 조회 예시
arr = [[1, 2, 3],
       [4, 5, 6, 7]]

print(arr)
print(len(arr))
print(len(arr[0]), len(arr[1]))
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])

# --------------------------------------------------

# N X M 배열의 크기와 저장된 값이 주어질 때 합을 구하는 방법
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0

for i in range(N):
    for j in range(M):
        s += arr[i][j]

# --------------------------------------------------

# 지그재그 순회

# i 행의 좌표
# j 열의 좌표
# 방법 1
# for i in range(n):
#     for j in range(m):
#         # 오름차순으로 할꺼면 [j + (m-1-2*j) * (i%2)] 여기에서 j 이후에 + 되는 값이 0이 되면 됨
#         # (i%2 가 그 역할을 함 / 짝수 홀수로 오름차순으로 할지 내림차순으로 할지 결정)
#         # => 그럼 range(m)으로 인해서 자동으로 우리가 원하는 값으로 j가 됨
#         # 내림차순으로 할꺼면 첫번째로 들어가는 값 [j + (m-1-2*j) * (i%2)]이 0이 아니라 m-1 이 되어야 함
#         f(array[i][j + (m-1-2*j) * (i%2)])

# 방법2
# for i in range(n):
#     if i % 2 == 1:
#         for j in range(m-1, -1, -1):
#             f(array[i][j])
#     else:
#         for j in range(m):
#             f(array[i][j])

