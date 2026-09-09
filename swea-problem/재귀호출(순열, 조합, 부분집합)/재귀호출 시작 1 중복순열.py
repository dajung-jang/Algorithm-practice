# 중복순열 [1, 1, 1] ~ [6, 6, 6]까지 출력하는 코드를 재귀호출로 구현해 보세요.
# [출력]
# 111
# 112
# ......
# ......
# 666


path = []

def KFC(lev):
    if lev == 4:
        print(*path)
        return

    for i in range(1, 7):
        path.append(i)
        KFC(lev + 1)
        path.pop()

KFC(1)

# ============= 강사님 풀이 ===============
# level: 3(주사위 3번), branch:6 (눈금이 6개)

path = []
def KFC(lev):
    if lev == 3:
        print(path)
        return
    for i in range(1, 7):   # 주사위가 1부터 6까지
        path.append(i)
        KFC(lev + 1)
        path.pop()

KFC(0)