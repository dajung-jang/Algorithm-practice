# 카운팅 정렬 : 강 항목이 몇개씩 있는지 세는 작업을 하여 정렬
# 핵심 : DAT 자료구조 활용
#
# DAT 자료구조란?
# : 값을 인덱스로 쓰는 자료구조
# 다음 배열을 하드코딩해 주세요.
# 카운팅 정렬 함수를 정의하여 호출해 보세요.
# 출력은 정렬된 결과를 출력합니다.
arr = [12, 3, 9, 1, 15, 7]

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val+1)

    for num in arr:
        count[num] += 1

    result = []

    for i in range(len(count)):
        result.extend([i] * count[i])

    return result

print(*counting_sort(arr))

# ------------- 강사님 풀이 ---------------------

def counting_sort(DATA, TEMP, k):

    DAT = [0] * (k + 1)

    # 1단계
    for i in range(len(DATA)):
        DAT[DATA[i]] += 1 # 값을 인덱스로, 갯수 counting

    # 2단계 : DAT값 조정 (누적)
    for i in range(1, k + 1):
        DAT[i] += DAT[i - 1]

    # 3단계 : 뒤에서부터 정렬된 배열 생성
    for i in range(len(DATA) - 1, -1, -1):
        DAT[DATA[i]] -= 1
        TEMP[DAT[DATA[i]]] = DATA[i]

DATA = [12, 3, 9, 1, 15, 7]
k = 15
TEMP = [0] * len(DATA) # 정렬된 결과를 저장할 배열

counting_sort(DATA, TEMP, k)

print(*TEMP)