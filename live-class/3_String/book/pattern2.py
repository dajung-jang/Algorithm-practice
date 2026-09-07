t = 'TTTTTATTAATA'
p = 'TZA'

# 방법1
def search(p, t):
    N = len(t)  # 텍스트의 길이
    M = len(p)  # 패턴의 길이
    for i in range(N-M+1):  # t에서 패턴을 비교할 시작 위치 인덱스 (비교 구간 시작 i)
        for j in range(M):      # p에서 비교할 위치 인덱스 (패턴 내부 비교 위치 j)
            if t[i+j] != p[j]:    # 다르면 다음 구간으로...
                break           # for j
        else:               # break에 걸리지 않고 for가 끝난경우 실행 (for j 가 정상 종료 했을 경우)
            return i        # 패턴이 처음 나타난 인덱스 리턴
    return -1               # t에 p패턴이 없는 경우 (일치하는 패턴 없음)

print(search(p, t))

# --------------------------------------

# 방법2
def brute_force(p, t):  # p 찾을 패턴, t 본문 문자열, 패턴이 있으면 인덱스, 없으면 -1 리턴
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    M = len(p)
    N = len(t)
    while j < M and i < N:
        if t[i] != p[j]:  # 다른 글자인 경우
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: return i - M  # 검색 성공
    else: return -1  # 검색 실패
print(brute_force(p, t))
