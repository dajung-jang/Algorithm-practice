# 0으로 채워진 8칸의 리스트를 만들어 주세요.
# for 문을 사용해서 앞의 4칸은 7로 채우고, 뒤의 4칸은 15로 채워 보세요.
#
# [입력]
#
# 없음
#
# [출력]
#
# 언패킹 연산자를 이용하여 출력해 주세요.

arr = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(4):
    arr[i] = 7

for j in range(4, 8):
    arr[j] = 15

print(*arr)

# 강사님 풀이
arr = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(4):  # 0, 1, 2, 3
    arr[i] = 7

for j in range(4, 8):   # 4, 5, 6, 7
    arr[j] = 15

print(*arr)