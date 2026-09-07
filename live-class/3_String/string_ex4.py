# 첫 줄에 N, 다음에 NxN 문자열. AB 패턴이 존재하는가?
#                            CD
def find_pat(text, N):
    pat = ['AB', 'CD']
    for i in range(N-1):    # 기분위치 i,j
        for j in range(N-1):
            cnt = 0
            for r in range(2):
                for c in range(2):
                    if text[i+r][j+c] == pat[r][c]:
                        cnt += 1
            if cnt == 4:
                return 'YES'
    return 'NO'

N = int(input())
text = [input() for _ in range(N)]

print(find_pat(text, N))

#  내가 짜본 코드 =>
# ans = 'NO'
# for i in range(N):
#     for j in range(N):
#         if text[i][j] == 'A' and text[i][j+1] == 'B' and text[i+1][j] == 'C' and text[i+1][j+1] == 'D':
#             ans = 'YES'
# print(ans)
