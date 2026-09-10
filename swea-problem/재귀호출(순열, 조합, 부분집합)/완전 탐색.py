# 정수 n을 입력받고, n개의 주사위를 던져 나올 수 있는 모든 경우에 대해,
# 합이 10 이하가 나오는 경우는 총 몇가지 인가요?
# 가능한 모든 케이스를 탐색한다. -> 완전 탐색 알고리즘 이라고 한다.
# [입력]
# 정수 한개를 입력받습니다.
# [출력]
# 합이 10 이하가 나오는 경우를 counting하여 출력합니다.


def KFC(lev):
    if lev == n:
        if sum(path) <= 10: return 1
        return 0

    cnt = 0

    for i in range(1, 7):
        path.append(i)
        cnt += KFC(lev + 1)
        path.pop()

    return cnt

path = []
n = int(input())
print(KFC(0))

# ============= 강사님 풀이 ===============


# Q) sum_v는 언제 누적될까?
# A) 재귀호출 할때 주사위값 i 누적

def KFC(lev, sum_v):
    # cnt = 0 # 재귀호출 할때마다 초기화
    global cnt # 전역변수 수정하려고

    # 가지치기 : 합이 이미 10초과하면 더이상 탐색을 진행하지 않음
    if sum_v > 10: return

    if lev == n: # 정점레벨에 도달했을때
        cnt += 1
        return

    for i in range(1, 7): # i = 1, 2, 3, 4, 5, 6
        path.append(i)
        # 재귀호출
        KFC(lev + 1, sum_v + i)
        path.pop()

path = []
cnt = 0
n = int(input())
KFC(0, 0)
print(cnt)