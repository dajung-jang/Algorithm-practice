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
arr = [2, 5, 1, 6, 4, 3]

sum_v = 0
max_v = float('-inf')   # 문제 조건에 없으면 음의 무한대 초기화
min_v = float('inf')    # 문제 조건에 없으면 양의 무한대 초기화

for i in arr:
    if i > max_v: max_v = i # 최대값 갱신 코드
    if i < min_v: min_v = i # 최소값 갱신 코드
    sum_v_v += i # 합계 누적

print(sum_v)
print(max_v - min_v)

