# 리스트를 하드코딩 해 주세요.
#
# 2 5 1 6 4 3
#
# 1. for문을 사용해서 전체 합을 출력해 보세요.
# 2. for문을 사용해서 최대값과 최소값의 차이를 출력해 보세요.
#
# <주의> 내장함수 사용 금지 (sum, max, min)
#
#
# [입력]
#
# 없음
#
# [출력]
#
# 합계
# 최대값 - 최소값

arr = [2, 5, 1, 6, 4, 3]
result_sum = 0

for i in arr:
    result_sum += i

print(result_sum)

result_min = arr[0]
result_max = arr[0]

for i in arr:
    if i < result_min:
        result_min = i

for j in arr:
    if j > result_max:
        result_max = j

print(result_max - result_min)

# 강사님 풀이