# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.
# 예를 들어 N=10, M=10 일 때, 다음과 같이 회문을 찾을 수 있다.
# GOFFAKWFSM
# OYECRSLDLQ
# UJAJQVSYYC
# JAEZNNZEAJ
# WJAKCGSGCF
# QKUDGATDQL
# OKGPFPYRKQ
# TDCXBMQTIO
# UNADRPNETZ
# ZATWDEKDQF
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N
# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

T = int(input())


def is_p(N, M, arr):
    for y in range(N):
        for x in range(N - M + 1):
            text = arr[y][x:x + M]
            if text == text[::-1]: return text

    for x in range(N):
        for y in range(N - M + 1):
            a = [arr[r][x] for r in range(y, y + M)]
            text = ''.join(a)
            if text == text[::-1]: return text

for i in range(T):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f'#{i+1} {is_p(N, M, arr)}')

# ============= 강사님 풀이 ===============

def is_p(text):
    return text == text[::-1]

def find_p(N, M):
    for y in range(N):
        for x in range(N-M+1):
            word=""
            # 단어의 길이만큼 순회
            for k in range(M): word += arr[y][x+k] # 단어 만들고 -> 회문인지 판별
            if is_p(word): return word

    for x in range(N):
        for y in range(N-M+1):
            word =""
            for k in range(M): word += arr[y+k][x                   ]
            if is_p(word): return word

    # 회문 찾지 못하면 빈문자열 반환
    return ""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 정수 아니니까 map 쓸 필요 없고, 공백 없으니까 split 쓸 필요 없음
    arr = [input() for _ in range(N)]
    result = find_p(N, M)
    print(f'#{tc} {result}')

