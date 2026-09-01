# for문을 사용해서 '#'을 9번 출력해 보세요.
# [입력]
# 없음
# [출력]
# ########

a = '#'
result = ""
for i in range(9):
    result += a

print(result)

# 강사님 풀이
for i in range(9):
    print('#', end='')
