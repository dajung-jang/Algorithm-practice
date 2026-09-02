# 정수 하나 n을 입력받고,
# n이 10보다 크면 '#'을 5번,
# n이 10이하면 '#'을 n번 출력해 주세요.
#
# 반드시 for문을 사용해 주세요.
#
# [입력]
#
# 정수 한개를 입력받습니다.
#
# [출력]
#
# n이 10보다 크면 '#' 5번 출력
# n이 10이하면 '#' n번 출력

n = int(input())

result = ""
if n > 10 :
    for i in range(5):
        result += "#"

else:
    for i in range(n):
        result += "#"

print(result)

# 강사님 풀이
N = int(input())

if n > 10:
    for i in range(5):
        print('#', end='')

else:
    for i in range(N):
        print('#', end='')
