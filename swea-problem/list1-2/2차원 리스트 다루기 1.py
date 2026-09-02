# 1. 0으로 채워진 4 x 4 (4행 4열) 2차원 배열을 만들어 주세요. (리스트컴프리헨션)
# 2. 다음과 같이 채워 주세요. (인덱싱)
# 3. 그대로 출력해 주세요.
# [입력]
# 없음
# [출력]
# 언패킹 연산자를 사용해 주세요.
# 7 0 0 0
# 0 0 0 1
# 0 3 0 0
# 0 0 0 9

arr = [[0] * 4 for _ in range(4)]
arr[0][0] = 7
arr[1][3] = 1
arr[2][1] = 3
arr[3][3] = 9

# 방법 1. 함수 사용
def result(a):
    for i in range(4):
        print(*a[i])

result(arr)

# 방법 2. 함수 미사용
for i in range(4):
    print(*arr[i])

# 강사님 풀이

arr = [[0] * 4 for _ in range(4)]
# 인덱싱
arr[0][0] = 7
arr[1][3] = 1
arr[2][1] = 3
arr[3][3] = 9

# row : 행
for row in arr:
    print(*row)