# 정수 하나 n을 입력받고,
# '#'를 n번 출력하고
# '!'를 n+5번 출력해 보세요.
#
# 반드시 for문을 사용해 주세요.
#
# [입력]
#
# 정수 한개를 입력받습니다
#
# [출력]
# '#' n번
# '!' n+5번

N = int(input())
x = ""
y = ""
for i in range(N):
    x += "#"

for i in range(N+5):
    y += "!"

print(x)
print(y)