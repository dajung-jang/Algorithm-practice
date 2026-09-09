# 아래처럼 1111~3333까지 출력하는 프로그램을 작성해 보세요.
# 방법 2가지
# 1. 중첩 for문
# 2. 재귀호출
# [출력]
# 1111부터 3333까지

# 중복 순열
# 방법 1(for 문)
for i in range(1, 4):
    for j in range(1, 4):
        for a in range(1, 4):
            for b in range(1, 4):
                print(i, j, a, b)

# 방법2
def f(i, N):
    if i == N:
        return
    else:
        print(i)
        f(i+1 ,N)


