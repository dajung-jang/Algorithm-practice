# 0 1 2 3 4 5 5 4 3 2 1 0을 재귀호출을 이용하여 구현해 보세요.
# 반드시 재귀호출과 기저조건을 구현합니다.
# [출력]
# 0 1 2 3 4 5 5 4 3 2 1 0

def f(i, N):
    if i == N:
        return
    else:
        print(i, end=' ')
        f(i+1, N)

def g(i):
    if i == -1:
        return
    else:
        print(i, end=' ')
        g(i-1)

f(0, 6), g(5)   # 그냥 ,로만 나열하면 자동으로 튜플로 인식함

# 오류 나는 코드
# def f(i, N):
#     if i == N:
#         if i == -1:
#             return
#         print(i-1, end=' ')
#         f(i-1, N)
#     print(i, end=' ')
#     f(i+1, N)
#
# f(0,6)

# ============= 강사님 풀이 ===============

def KFC(lev):
    if lev == 6:
        return
    print(lev, end=' ')
    KFC(lev + 1)    # 재귀호출되면서 1 증가
    print(lev, end= ' ')   # 함수종료되면서 함수 특징 2번 값만 복사된다

KFC(0)