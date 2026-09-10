# 쵸파에게는 3명의 친구가 있습니다.
# 'Luffy' 'Zoro' 'Sangi'
# 함께 영화관에 갈 수 있는 멤버를 구성하고자 합니다.
# 모든 경우의 수를 출력해 보세요.
# 완전탐색을 이용하여 구현합니다.
# (단, 쵸파 혼자 영화관에 갈 수 도 있습니다.)
# [출력]
# 모든 부분집합

# 생각을 해보자.... 일단 초파 혼자서도 갈 수 있으니까 공집합 포함인거고


# ============= 강사님 풀이 ===============

arr = ['O', 'X']
path = []
name = ['Luffy', 'Zoro', 'Sanji']

def print_name():
    for i in range(3):
        if path[i] == 'O': print(name[i], end = ' ')
    print()


# branch가 2고, level이 3인 중복순열 코드
def KFC(lev):
    # 정점 레벨에 도달 했을 때 부분집합 출력
    if lev == 3:
        print_name()
        return

    for i in range(2):
        path.append(arr[i])
        KFC(lev + 1)
        path.pop()

KFC(0)