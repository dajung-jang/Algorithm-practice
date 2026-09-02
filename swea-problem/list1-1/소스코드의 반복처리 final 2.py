# 정수 n을 입력받고,
# n이 짝수면 n이 2씩 증가하면서 5개 더 출력하고,
# n이 홀수면 n이 3씩 증가하면서 10개 더 출력해 보세요.
#
# 반드시 for문을 사용해 주세요.
#
# [입력]
#
# 정수 한개를 입력받습니다.
#
# [출력]
#
# n이 짝수면
# n n+2 n+4 ..... (총 6개)
# n이 홀수면
# n n+3 n+6 ..... (총 11개)

n = int(input())

result = [n]

if n % 2 == 0:
    for i in range(5):
        n = n+2
        result.append(n)

else:
    for i in range(10):
        n = n+3
        result.append(n)

print(*result)

# 강사님 풀이
n = int(input())

if n % 2 == 0:
    for i in range(6):
        print(n + 2*i, end=' ')     # 2배된거 더하기

else:
    for i in range(11):
        print(n + 3 * i, end = ' ')     # 3배 된 거 더하기
