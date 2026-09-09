# 아래처럼 11~33까지 출력하는 프로그램을 작성해 보세요.
# [출력]
# 11부터 33까지

# 방법 1. for 문 사용
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i,j)

# 방법 2. 함수 사용
def f(i, j, N):
    if j == N:
        return
    else:
        print(i, j)
        f(i, j+1, N)

def g(i, N):
    if i == N:
        return
    else:
        # 및에 g(1, 4)로 한것처럼 처음 j 값을 1로 지정해줘야하는데 그렇게 한 곳이 없으니 여기서 지정해줘야함 / i 가 일일때 f() 돌려서 j가 1인걸로 처음 넣어주면 알아서 j가 3인것 까지  실행하고 i=1 일때는 끝나고 여기로 돌아옴 그러고 i+1을 해주고 또 j=1 인것부터 다시 시작
        f(i, 1, N)
        g(i+1, N)

g(1, 4)