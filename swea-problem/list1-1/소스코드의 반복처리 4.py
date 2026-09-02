# 정수 a와 b를 입력 받고,
# a가 b 이하면 a부터 b까지 출력(증가)
# a가 b보다 크면 a부터 b까지 출력(감소)
#
# 반드시 for문을 사용해 주세요.
#
# [입력]
# 정수 a와 b를 공백을 기준으로 입력받습니다.
#
# [출력]
# a가 b이하 : a~b출력(증가)
# a가 b초과 : a~b출력(감소)

a, b = map(int, input().split())
numbers = ""

if a <= b:
    for i in range(a, b+1):
        numbers += str(i)

else:
    for i in range(a, b-1, -1):
        numbers += str(i)

result = " ".join(numbers)
print(result)

# 강사님 풀이
# map 함수 쓰는 이유 : 입력받은 문자열을 정수로 바꾸려고
# split() 쓰는 이유 : 공백 기준으로 입력 받으려고
x, y = map(int, input().split())

if x <= y:
    for i in range(x, y+1):
        print(i, end=' ')
else:
    # y-1 을 포함하지 않으면 y까지
    for j in range(x, y - 1, -1):
        print(j, end=' ')
