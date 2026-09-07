# 문자열 하나를 입력받고, 회문인지 아닌지 판별하여
# 회문이면 1, 회문이 아니면 0을 출력해 보세요.
# 회문 판별 함수를 만들어 주세요.
# (회문 : 거꾸로 읽어도 같은 문자열)
# [입력]
# 문자열 하나를 입력받습니다.
# [출력]
# 회문이면 1, 회문이 아니면 0

text = input()

def is_p(text):
    return text == text[::-1]

print(int(is_p(text)))

# ============= 강사님 풀이 ===============

def is_palindrome(text):
    if text == text[::-1]:
        return 1
    return 0

text = input()

print(is_palindrome(text))