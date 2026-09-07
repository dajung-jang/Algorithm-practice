# 다음 문자열을 하드코딩 해 주세요.
# 문자열 text에서 'KFC'가 몇 번째 인덱스에 있는지 출력해 보세요.
# 메서드를 사용해 주세요.
# [입력]
# 없음
# [출력]
# 'KFC'가 처음 발견되는 인덱스

text = 'BBQBHCKFCMC'

n = text.find('KFC')
print(n)

# ============= 강사님 풀이 ===============
text = 'BBQBHCKFCMC'

print(text.find('KFC'))
