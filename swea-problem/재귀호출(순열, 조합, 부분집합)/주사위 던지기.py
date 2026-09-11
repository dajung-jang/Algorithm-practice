# 주사위를 N개 던져서 나올 수 있는 모든 조합을 출력해 보세요.
# [입력]
# 정수 한개를 입력 받습니다.
# [출력]
# 조합 출력




# ============= 강사님 풀이 ===============

N = int(input())

path = []

def KFC(lev, start):
    if lev == N :   # level: N
        print(*path)
        return

    for i in range(start, 7):   # branch: 최대 6, 최소 1
        if used[i] == 1: continue
        path.append(i)
        KFC(lev + 1, i)
        path.pop()

KFC(0, 1)   # 주사위 눈금 1부터

# ------------------------------
# 만약에 used 배열 쓰면 -> 중복 없는 조합

N = int(input())

# stack 자료구조 응용
path = []
# dat 자료구조 응용
used = [0] * 7  # 1부터 6이니까

def KFC(lev, start):
    if lev == N :   # level: N
        print(*path)
        return

    for i in range(start, 7):   # branch: 최대 6, 최소 1
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        KFC(lev + 1, i) # i는 주사위
        path.pop()
        used[i] = 0

KFC(0, 1)   # 주사위 눈금 1부터