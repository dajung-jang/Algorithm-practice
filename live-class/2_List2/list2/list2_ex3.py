arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9, 12]
N = len(arr)

ans = 'N'
for i in range(1, 1 << N): # 2**N, 부분집합을 표현할 비트(2진수) 생성 / 앞에 1, 을 붙으면 공집합은 제거
    s = 0   # 부분집합의 합 저장할 변수
    for j in range(N):  # 검사할 비트 번호 j
        if (i & (1 << j)):  # j번 비트가 1이면 arr[j]가 부분집합의 원소
            s += arr[j]
    if s == 0:
        ans = 'Y'
        break   # for i

print(ans)

