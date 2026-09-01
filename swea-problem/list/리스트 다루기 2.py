# 9 5 1 15 7 3
# 리스트를 하드코딩 해주세요

# 리스트를 for문을 사용해서 거꾸로 출력해 보세요.
# 그리고, len함수를 사용해 주세요.
#
#
# [입력]
#
# 없음
#
# [출력]
#
# 리스트를 거꾸로 출력

arr = [9, 5, 1, 15, 7, 3]

for i in range(len(arr)-1, -1, -1):
    print(arr[i], end=' ')

# 강사님 풀이
arr = [9, 5, 1, 15, 7, 3]

# len(arr) - 1 : 마지막  element 의 index
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end = ' ')

