# 다음 문자열을 하드코딩 해 주세요.
# 금을 찾아라!!!
# GOLD는 총 몇개 있을까요?
# count() 메서드 사용 금지, find() 메서드를 사용해 주세요.
# [출력]
# GOLD의 갯수

text = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']

# 첫번째 풀이
def get_find(text):
    cnt = 0
    for i in range(3):
        j = 0
        while j < len(text[i]):
            idx = text[i].find('GOLD', j)
            if idx == -1 : break
            elif j == idx:
                cnt += 1
                j += 4
            else: j += 1
    return cnt

print(get_find(text))

# 두번째 풀이
def get_find(word):
    cnt = 0
    i = 0
    while i < len(word):
        idx = word.find('GOLD', i)
        if idx == -1 : break    # -1 반환되면 word 안에 gold 가 없다는 뜻이니까 그냥 while 문 빠져나가기
        elif i == idx:
            i += 4
            cnt += 1
        else : i += 1
    return cnt

sum_v = 0

for word in text:
    sum_v += get_find(word)

print(sum_v)
# ============= 강사님 풀이 ===============

arr = ['GOLDABCGOLD', 'HELLOWORLD', 'WHITEGOLD']

def get_count(word):
    cnt = 0
    for text in arr:
        a = 0
        while True:
            b = text.find(word, a)
            if b == -1: break
            cnt += 1
            a = b + 1
    return cnt

print(get_count('GOLD'))

