# 트리형태를 보고 직접 재귀호출 코드를 구현해 보세요.
# 핵심 : branch, level을 확인후 직접 구현합니다.
# 재귀 호출 함수가 종료되면서 올라올 때의 레벨을 출력해 주세요.
# [출력]
# 2
# 2
# 1
# 2
# 2
# 1
# 0

def f(lev):
    if lev == 3:
        return

    for i in range(2):
        f(lev + 1)



f(0)

# ============= 강사님 풀이 ===============

def f(lev):
    if lev == 3:
        return

    for i in range(2):
        f(lev + 1)

    print(lev)

f(0)  # 0 level 부터