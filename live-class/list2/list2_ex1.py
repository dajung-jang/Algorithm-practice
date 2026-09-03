# 5x5 2차원 배열에 25개의 숫자를 저장하고, 대각선 원소의 합을 구하시오

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 대각선
ans = 0
for i in range(N):
    ans += arr[i][j] + arr[i][N-1-i]

# 중복으로 더해진 값 뺌(N이 짝수일때는 겹치는 값 없음)
if N % 2:   # N이 홀수인 경우에만 중심 원소가 겹치니까 빼주는거 if 로 조건 거는거임(값이 0, 1 일때만 저렇게 ==0 이런거 안붙여줘도 됨 0은 false, 다른 숫자는 true 로 인식
    ans -= arr[N // 2][N // 2]

