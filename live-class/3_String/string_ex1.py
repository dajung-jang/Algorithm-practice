# 두 개의 문자열 s1과 s2. s1의 각 글자가 s2에 모두 존재하는가

s1 = input()
s2 = input()

# 모두 있다고 가정하고, 하나라도 없으면 'NO'로 바꾸고 종료
ans = 'YES'
for ch in s1:
    if ch not in s2:
        ans = 'No'
        break   # for ch 를 중단
print(ans)
