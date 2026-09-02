N = int(input())
arr = list(map(int, input().split()))

max_idx = 0     # 첫 원소를 최댓값으로 가정
for i in range(1, N):
    if arr[max_idx] <= arr[i]:  # 최댓값이 여러개면 마지막 위치
        max_idx = i

print(max_idx)