# 다음은 연결되어 있는 두 개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다.
# 모든 정점을 깊이 우선 탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시어
# 7 8                               # 정점 수, 간선수
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7   # 간선 양 끝 정점
# 출력 결과의 예는 다음과 같다
# : 1 2 4 6 5 7 3

# 탐색하는 함수 정의
def dfs(v):
    print(v, end=' ')
    visited[v] = 1
    # v 에 인접하고 방문 안한 w
    for w in adj_list[v]:   # 저장한 순서대로
        if visited[w] == 0: # 방문 안한 곳
            dfs(w)

# E= edge(간선 수) / V = 정점 수
V, E = map(int, input().split())
graph = list(map(int, input().split()))
# adj_list= 인접 리스트를 의미
adj_list = [[] for _ in range(V+1)]
for i in range(E):
    v, w = graph[i*2], graph[i*2+1]

    adj_list[v].append(w)
    adj_list[w].append(v)   # 방향이 없는 경우 추가

visited = [0] * (V + 1)

print(dfs(1))