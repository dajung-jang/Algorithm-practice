# 배열을 다음과 같이 하드코딩 해 주세요.
# 정수 n을 입력받고, n이 배열 A에 몇개 있는지 counting하는 get_count(n) 함수 만들기
# <주의> count() 메서드 사용 금지
# [입력]
# 정수 한개를 입력 받습니다.
# [출력]
# counting 결과를 출력합니다.

A = [5, 2, 5, 7, 3]

n = int(input())

def get_count(n):
    c = 0
    for i in A:
        if i == n: c += 1
    return c

print(get_count(n))

# ------------- 강사님 풀이 ---------------------

A = [5, 2, 5, 7, 3]

def get_count(n):
    cnt = 0
    for i in range(5):
        if A[i] == n: cnt += 1

    return cnt

n = int(input())
ret = get_count(n)
print(ret)