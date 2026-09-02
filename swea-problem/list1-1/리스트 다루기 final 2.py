# 빈 리스트 arr를 만들어 주세요.
# 정수 a와 b를 입력받고,
# for문을 사용해서 a 3칸, b 2칸, a+b 3칸 채워 보세요.
#
#
# [입력]
#
# 정수 a와 b를 입력받습니다.
#
# [출력]
#
# a a a b b a+b a+b a+b
# 언패킹 연산자를 사용해서 출력해 주세요.

# 풀이 1

arr = []

# 처음엔 그냥 빈 배열로만 정의 했는데 배열에 값이 없으면 arr에서 인덱스 지정해서 값 넣는게 안됨
# 리스트에 인덱스로 값 할당하려면 그 인덱스에 이미 요소가 있어야하는데
# 그게 아니었어서 arr[0] = a 가 작동 안되는거임
# 그래서 arr = [0] * 8 해서 리스트를 [0, 0, 0, 0, 0, 0, 0, 0]로 만들어준거임
arr = [0] * 8
a, b = map(int, input().split())

for i in range(3):
    arr[i] = a

for j in range(3, 5):
    arr[j] = b

for k in range(5, 8):
    arr[k] = a + b

print(*arr)

# 풀이2
# append를 사용하는 방법으로 다시 짠거

arr = []

a, b = map(int, input().split())

for _ in range(3):
    arr.append(a)

for _ in range(2):
    arr.append(b)

for _ in range(3):
    arr.append(a + b)

print(*arr)

# 강사님 풀이
a, b = map(int, input().split())
arr = []

for i in range(3):
    arr.append(a)

for i in range(2):
    arr.append(b)

for i in range(3):
    arr.append(a+b)

print(*arr)