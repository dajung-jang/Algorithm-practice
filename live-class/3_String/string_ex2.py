# 첫 줄에 N, 다음에 NxN 문자열 . 'Z'가 존재하는가?

N = int(input())
text = [input() for _ in range(N)]

# 방법 1
ans = 'NO'
for row in text:
    if 'Z' in row:
        ans = 'YES'
        break   # for row 중단
print(ans)

# 방법 2(이중 for 문은 break 썻을때 안쪽 for문만 중단 되기 때문에 함수로 묶어서 return으로 해주면 좋음
def find_Z(text, N):
    for i in range(N):
        for j in range(N):
            if text[i][j] == 'Z':
                return "YES"
    return "NO"

