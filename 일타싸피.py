import math

# 1. rad을 degree로 degree를 rad으로 바꾸는 법
print(math.pi) # 라디안 pi : 3.14
degree = 30
# rad = 30 * (math.pi / 180) : 공식
rad = math.radians(degree) # 공식대신 메서드
print(rad)
degree = math.degrees(rad) # 공식대신 degree로 변환

# 2. sin, cos, tan
print(f'{math.sin(rad):.1f}')
print(f'{math.cos(rad):.1f}')
print(f'{math.tan(rad):.1f}')

# 2. sin, cos, tan
print(f'{math.sin(rad):.1f}')
print(f'{math.cos(rad):.1f}')
print(f'{math.tan(rad):.1f}')

# 3. 피타고라스 정리 (두 변의 길이를 알 때 나머지 한변의 길이 구하기_
# b 와 c 를 알고 a를 구하고 싶다

b = 4
c = 5
# 식 a**2 + b**2 = c**2
# a**2 = c**2 - b**2
# 양 변에 루트 씌우기 ( 루트: sqrt)
a = math.sqrt(c**2 - b**2)
print(a)

# 4. 삼각함수의 역함수 (변의 길이를 알고 각도를 알고 싶을 때)
print(math.asin(a/c))
print(math.acos(a/c))
print(math.atan(a/c))

# 이건 알고 있어야 함!!!
# 직경: 지름
# 당구대 플레이 영영 = 254 * 127
# 공 직경: 5.73
# 코딩 시 좌표의 1.0 dms 1cm를 의미