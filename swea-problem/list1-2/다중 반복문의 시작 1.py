# 정수 n을 입력받고, 2중 for문을 사용하여
# '#'으로 이루어진 n x n 행렬을 출력해 보세요.
#
# [입력]
#
# 정수 한개를 입력받으세요.
#
# [출력]
#
# '#'으로 이루어진 n x n 행렬

n = int(input())
for _ in range(n):
    for _ in range(n):
        print('#', end='')
    print()
