# N x N 사각형의 전투장에는 각 칸마다 몇 마리의 몬스터가 있는지 적혀 있다.
# 광대한 영역에 마법을 시전할 수 있는 마법사 Mort 는 전투장에서 최대한 많은 몬스터를 잡으려한다.
# 마법사 Mort는 대각선 방향으로 각 방향마다 K 칸 만큼 마법을 시전할 수 있다.
# 마법은 마법사가 있는 지점에서 마법을 시전한 위치를 제외하고
# 대각선 방향으로 방향 변화 없이 시전된다.
# 예를들어 [그림1]와 같은 5 x 5 인 전투장에서
# 노란색으로 표시된 2번 행 2번 열에서 K = 2 인 마법을 시전하게되면
# 각 방향마다 2칸씩 , [그림2] 와 같이 몬스터를 공격하게 되며
# 총 1 + 10 + 7 + 2 + 2 + 2 + 1 + 1 = 26 마리를 처치하게 된다.
# 반면에 [그림3]와 같이 0번 행 2번 열에서 K = 2인 마법을 시전하면 [그림4] 와 같이 아래 대각선 방향 K칸에 해당되는몬스터를 공격하게 되며
# 총 7 + 2 + 0 + 7 = 16 마리 몬스터를 처치할 수 있다.
# 마법사 Mort 씨가마법을 한번 시전하여처치할수 있는 몬스터의 최대 수를 출력하시오.
# 입력
# 첫째줄에 전투장의 가로세로크기인 N 이 입력된다. (1 <= N <= 100)
# 다음 줄부터는 N 줄에 걸쳐 각줄마다 N개의 정수가 공백으로 구분되어 입력된다. ( 0<= 정수 <= 100,000)
# 마지막 줄에는 마법의 시전범위 K 가 입력된다. (1 <= K <= 100)
# 출력
# 마법사가 잡을 수 있는 몬스터의 최대 수를 출력하시오.

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

dy = []
dx = []

# dy, dx 배열 생성
for k in range(1, K+1):
    # extend는 append랑 다르게 안에 있는 원소들을 풀어서 꺼내서 이어 붙이는거여서 리스트 안에 리스트가 들어가는게 아니라 숫자들을 그대로 한줄로 붙임
    #    -> dy.append([-k, k, k, -k]) 하면 dy = [[], [], []] 이런식으로 덩어리로 추가 됨
    dy.extend([-k, k, k, -k])
    dx.extend([k, k, -k, -k])

    # 아래 코드 8줄이랑 동일한 기능을 하는 위의 코드 2줄
    # dy.append(-k)
    # dy.append(k)
    # dy.append(k)
    # dy.append(-k)
    # dx.append(k)
    # dx.append(k)
    # dx.append(-k)
    # dx.append(-k)

max_v = 0

for y in range(N):
    for x in range(N):
        # 인덱스 [y][x]인 곳을 기준으로 각 대각선 칸의 인덱스 값 생성(ny, nx)
        sum_v = 0
        for i in range(K * 4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            sum_v += arr[ny][nx]
        if max_v < sum_v: max_v = sum_v

print(max_v)

# ------------- 강사님 풀이 ---------------------

N = int(input()) # N행
arr = [list(map(int, input().split())) for _ in range(N)] # N행 2차원 배열
K = int(input()) # 마법이 퍼져나가는 세기

def magic(y, x):
    # 대각선
    dy = [-1, 1, -1, 1]
    dx = [1, 1, -1, -1]
    sum_v = 0

    for i in range(4): # 대각선 4방향
        for j in range(1, K+1): # j는 마법이 퍼져나가는 정도
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            sum_v += arr[ny][nx]
    return sum_v

# 구현 부분
result = float('-inf')
# 행순회
for i in range(N):
    for j in range(N):
        # 최대값
        result = max(result, magic(i, j))

print(result)
