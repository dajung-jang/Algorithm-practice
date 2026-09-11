# 0 ~ 9 의 번호가 적혀있는 카드가 6장 있다.
# 예시 : 0 1 7 2 7 7
# 3 장의 카드가 연속적인 번호를 갖는 경우 “run” 이라고 하고,
# 3 장의 카드가 동일한 번호를 갖는 경우는 “triplet” 이라고 한다.
# 그리고 6장의 카드가 run과 triplet로만 구성된 경우를 “baby-gin”으로 부른다.
# (위 예시에서는 0 1 2 와 7 7 7 카드가 있으므로 baby-gin 이다.)
# 6장의 카드 번호를 입력 받고,
# 완전탐색으로 baby-gin 여부를 판단하는 프로그램을 작성하라.
# [입력 예시]
# 6 6 7 7 6 7
# 666, 777 로 묶으면 두 개의 triplet이므로 baby-gin 이 발견되었다.
# 따라서 출력 결과는 Yes 이다.
# 0 5 4 0 6 0
# 456, 000 으로 묶으면 run과 triple이므로 baby-gin이 발견되었다.
#      따라서 출력 결과는 Yes 이다.
# 1 0 1 1 2 3
# 한 개의 triplet(111)이 존재하나, 나머지 023이 triplet, run이 아니다.
# 한 개의 run(123)이 존재하나, 나머지 011이 triplet, run이 아니다.
# 한 개의 run(012)이 존재하나, 나머지 113이 triplet, run이 아니다.
# 어떤 묶음으로 baby-gin을 찾아낼 수 없었기에, 출력결과는 No 이다.
# 완전 탐색을 이용하여, baby-gin 여부를 검사하는 프로그램을 작성하시오.
# [풀이 힌트 1]
# 고려할 수 있는 모든 경우의 수 생성하기
# 6개의 카드로 만들 수 있는 모든 순서를 나열
# = “순열＂코드를 작성한다.
# 예) 입력으로 2 3 5 7 7 7 을 받았을 경우,
# 아래와 같이 순열을 생성할 수 있다.
# [풀이 힌트 2]
# 검사하는 함수를 제작하여 하나씩 테스트
# is_baby_gin( ) 함수를 제작한다.
# 앞에 3 자리가 run 또는 triplet 이면서
# 뒤에 3 자리가 run 또는 triplet 이면 True를 리턴한다.
# 그렇지 않으면 False를 리턴한다.
# 많은 순열 중, 하나라도 통과된다면 Baby-gin 이 맞다.
# 6자리 숫자를 입력 받은 후, 완전탐색을 적용하여
# Baby-gin 여부를 검사하는 프로그램을 작성하시오.
# Yes / No 를 출력한다.
# [입력 / 출력 예시]
# 1 2 4 7 8 3 -> No
# 6 6 7 7 6 7 -> Yes
# 0 5 4 0 6 0 -> Yes
# 1 0 1 1 2 3 -> No

# --------

# 문제 생각해보자
# 일단 주어진 카드를 오름차순으로 재배열을 해야한다 그래야 연속적인 번호이거나 동일한 번호일때 판단할 수 잇으니까
# baby gin 이려면 앞의 세개가 연속적이거나 뒤의 세개가 연속적이어야한다 0,1,2 / 3,4,5
# 그러고 남은게 같은 숫자여야한다

# 오... 런타임 오류,ㅡ,,,
arr = list(map(int, input().split()))

arr.sort()

def gin(arr):
    if arr[0] == arr[1] == arr[2]:
        if arr[3] + 1 == arr[4] == arr[5] -1 or arr[3] == arr[4] == arr[5]:
            print('Yes')
        else: print('No')
    elif arr[3] == arr[4] == arr[5]:
        if arr[0] + 1 == arr[1] == arr[2] -1:
            print('Yes')
        else: print('No')
    elif arr[0] + 1 == arr[1] == arr[2] -1:
        if arr[3] + 1 == arr[4] == arr[5] -1:
            print('Yes')
    else: print('No')

gin(arr)

# ============= 강사님 풀이 ===============

# 숫자를 6번 나열한다 -> level:6
# 6장의 카드 -> branch:6

arr = list(map(int, input().split()))
used = [0] * 6  # 0번 인덱스부터 5번까지 쓸거기땜에
path = []
is_found_baby_gin = False

def is_baby_gin():  # baby-gin 이냐?
    cnt = 0
    # 앞에 세자리가 triple 또는 run 이라면 cnt += 1
    a, b, c = path[0], path[1], path[2]
    if a == b == c: cnt += 1
    elif a == (b-1) == (c-2): cnt += 1

    # 뒤에 세자리가 triplet 또는 run 이라면 cnt += 1
    a, b, c = path[3], path[4], path[5]
    if a == b == c: cnt += 1
    elif a == (b - 1) == (c - 2): cnt += 1

    # 만약 count가 2라면 baby-gin 이 맞음
    return cnt==2   # 판별식 -> 결과값: True or False


def KFC(lev):
    if lev == 6:    # 정점 레벨에 도달했다 == 카드 6장 다 나열했다
        if is_baby_gin(): is_found_baby_gin = True
        return
    for i in range(6):
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        KFC(lev+1)
        path.pop()
        used[i] = 0

KFC(0)

if is_found_baby_gin: print('Yes')
else: print('No')