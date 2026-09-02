# 1. 정수 여러개를 입력받아 리스트에 채워 주세요.
# 2. 7이 몇개인지 counting 해 보세요.
#
#
# [입력]
#
# 정수를 공백을 기준으로 입력받습니다.
#
# [출력]
#
# 리스트에 7이 몇개 인지 counting하여
# cnt변수 출력해 주세요.

cnt = 0
arr = map(int, input().split())

for i in arr:
    if i == 7: cnt += 1

print(cnt)

# 강사님 풀이

# 공백을 기준으로 입력받고 -> 정수로 형변환 -> 리스트에 담기
arr = list(map(int, input().split()))

cnt = 0
for a in arr:
    if a == 7: cnt += 1
