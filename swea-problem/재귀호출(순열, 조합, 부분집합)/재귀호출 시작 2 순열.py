# 정수 n을 입력받고, n개의 주사위를 던져 나올 수 있는 순열을 출력해 보세요.
# [입력]
# 정수 한개를 입력받습니다.
# [출력]
# 순열

n = int(input())

def f(lev):
    if lev == n:
        print(*path)
        return

    for i in range(1, 7):
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        f(lev + 1)
        path.pop()
        used[i] = 0

path = []
used = [0] * 7

f(0)

# ============= 강사님 풀이 ===============
def KFC(lev):
    if lev == n: # level:n
        print(*path)
        return

    for i in range(1, 7): # branch:6
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        KFC(lev + 1)
        path.pop()
        used[i] = 0

n = int(input()) # level
path = []
used = [0] * 7 # 1부터 6까지
KFC(0)