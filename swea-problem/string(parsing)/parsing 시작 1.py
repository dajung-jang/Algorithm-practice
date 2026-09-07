# 다음 문자열을 하드코딩 해 주세요.
# 문자열 text에서 대괄호 안에 있는 숫자를 추출해 보세요.
# find() 메서드를 사용해 주세요.
# [입력]
# 없음
# [출력]
# 대괄호 안의 숫자

text = 'helloworld[92084]answer'

n1 = text.find('[')
n2 = text.find(']')

print(text[n1+1:n2])

# ============= 강사님 풀이 ===============

text = 'helloworld[92084]answer'

# '[' 위치 찾기
start_idx = text.find('[') + 1
end_idx = text.find(']')

num = text[start_idx:end_idx]

print(num)