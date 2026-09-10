arr = input().split()
n = len(arr)

def get_sub(i): #부분집합을 달라
    for j in range(n):
        if i & (1 << j):
            subset.append(arr[j])
    return subset

cnt = 0

for tar in range(1 << n):
    subset = [] # 부분집합 저장해놓을 배열
    get_sub(tar)
    if len(subset) >= 2:
        cnt += 1

print(cnt)

# ============= 강사님 풀이 ===============

arr = input().split()
n = len(arr)

def get_count(i):
    cnt = 0
    for j in range(n):
        # i의 j번째 비트가 1이면 카운트 증가
        if i & (1 << j): cnt += 1

    return cnt

result = 0
for tar in range(1 << n):
    # 2명 이상
    if get_count(tar) >= 2 : result += 1

print(result)