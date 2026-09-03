# 배열을 다음과 같이 하드코딩 해 주세요.
# 배열 A의 각각의 element가 배열 B의 element와 같은지 판별하는 is_exist(n) 함수 만들기
# [출력]
# 맞으면 'O' 틀리면 'X'

A = [5, 7, 5, 4, 2, 9]
B = [5, 4, 2, 5, 6]

def is_exist():
    result = ['X'] * 6
    for i in B:
        for j in range(6):
            if i == A[j]: result[j] = 'O'
    return result

print(*is_exist())

# ------------- 강사님 풀이 ---------------------

A = [5, 7, 5, 4, 2, 9]
B = [5, 4, 2, 5, 6]

def is_exist(n): # 존재하냐?
    for i in range(5): # B가 5개
        if B[i] == n: return 1

    return 0

for i in range(6):# A가 6개
    if is_exist(A[i]): print('O', end = ' ')
    else: print('X', end = ' ')