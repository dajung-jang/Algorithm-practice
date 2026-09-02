# 다음과 같이 하드코딩 해 주세요.
# A B Q T
# 2중 for문을 사용하여 다음과 같이 역순으로 출력해 보세요.
#
# TQBA
# TQBA
# TQBA
# TQBA
#
# [입력]
# 없음
# [출력]
# 역순으로 출력하는 소스코드를 4번 반복합니다.

arr = ['A', 'B', 'Q', 'T']

for _ in range(4):
    for i in range(3, -1, -1):
        print(arr[i], end='')
    print()

# 강사님 풀이 (slicing 으로도 가능 [::-1])
arr = ['A', 'B', 'Q', 'T']

for i in range(4):
    for j in range(3, -1, -1):
        print(arr[j], end='')
    print()
