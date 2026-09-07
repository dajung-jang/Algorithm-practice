# 다음 문자열을 하드코딩 해 주세요.
# 다음 배열의 모든 element에서 대괄호 안에 있는 숫자만 출력해 보세요.
# find() 메서드를 사용해 주세요.
# get_find(text) 함수를 만들어 주세요.
# [입력]
# 없음
# [출력]
# 대괄호 안의 숫자를 순서대로 출력

arr = ['ABCQ', 'B[4]R', 'CCDA', 'BT[15]']
result = []

def get_find(text):
    for i in range(len(arr)):
        n1 = arr[i].find('[')   # find()에서 결과 없으면 -1 반환하는거 잊지 말기
        n2 = arr[i].find(']')

        if n1 != -1 and n2 != -1:   # -1 아닐때만 실제 제대로 인덱스가 나온거니까 조건 걸러주기
            n = arr[i][n1 + 1:n2]
            result.append(n)

    return result

print(*get_find(arr))

# ============= 강사님 풀이 ===============

def get_find(text):
    if text.find('[') == -1: return ""  # 빈문자열
    start = text.find('[') + 1
    end = text.find(']')
    return text[start:end]  # 슬라이싱

for text in arr:
    result = get_find(text)
    # 0, 0.0, ""  -> False
    if result: print(result, end=' ')