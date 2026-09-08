# 다음 문자열을 하드코딩 해 주세요.
# 문자열 text에서 대괄호 안에 있는 숫자들의 합을 출력해 보세요.
# (예 : 45 + 9994 = 10039)
# find() 메서드를 사용해 주세요.
# [입력]
# 없음
# [출력]
# 대괄호 안의 숫자들의 합

text = 'B[45]AB[9994]'

x1 = text.find('[')
y1 = text.find(']')
x2 = text.find('[', x1+1)
y2 = text.find(']', y1+1)

n1 = text[x1+1:y1]
n2 = text[x2+1:y2]

result = int(n1) + int(n2)

print(result)

# ============= 강사님 풀이 ===============

idx1 = text.find('[')
idx2 = text.find(']', idx1 + 1)
idx3 = text.find('[', idx2 + 1)
idx4 = text.find(']', idx3 + 1)

num1 = text[idx1+1:idx2]
num2 = text[idx3+1:idx4]

print(int(num1) + int(num2))


