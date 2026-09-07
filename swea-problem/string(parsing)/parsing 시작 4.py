# 다음 문자열을 하드코딩 해 주세요.
# 문자열 text에 문자열 'ABC'가 몇개 있는지 출력해 보세요.
# 1. count() 메서드 사용 금지, find() 메서드를 사용해 주세요.
# 2. while break를 활용해 주세요
# [입력]
# 없음
# [출력]
# 문자열 'ABC'의 갯수

text = 'ABCDEFABCKKKKKABC'

i = 0
cnt = 0
while i < len(text):
    if text.find('ABC', i) != -1:
        cnt += 1
    else: break
    i += 1


print(cnt)
# ============= 강사님 풀이 ===============



