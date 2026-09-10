# Forth라는 컴퓨터 언어는 스택 연산을 기반으로 하고 있어 후위 표기법을 사용한다. 예를 들어 3+4는 다음과 같이 표기한다.
# 3 4 + .
# Forth에서는 동작은 다음과 같다.
# 숫자는 스택에 넣는다.
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# ‘.’은 스택에서 숫자를 꺼내 출력한다.
# Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
# 다음은 Forth 연산의 예이다.
#  코드        출력
# 4 2 / .       2
# 4 3 - .       1
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
# 나눗셈의 경우 항상 나누어 떨어진다.
# [출력]
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

# 이거 완성 코드 아님
T = int(input())

for i in range(1, T+1):
    text = input().split()
    stack = []

    for x in text:
        if x == '.': break
        elif x not in '(+-*/)':
            stack.append(x)
        else:
            if len(stack) < 2 :
                print("error")
                break
            a = int(stack.pop())
            b = int(stack.pop())
            if x == '+':
                stack.append(b + a)
            elif x == '*':
                stack.append(b * a)
            elif x == '-':
                stack.append(b - a)
            elif x == '/':
                stack.append(b / a)


    print(f'#{i} {stack[0]}')

# ============= 강사님 풀이 ===============

# 피연산자(숫자)는 스택에 push
# 연산자 만나면 스택에서 두개의 숫자를 pop 해서 계산
# 계산 결과를 다시 스택에 push
# 마지막에 스택에는 딱 하나의 결과값만 있어야함
# len(stack) == 1 이어야함

# ex) "1 2 + 3 * ."
# 1. '1' : 스택에 push => stack = [1]
# 2. '2' : 스택에 push => stack = [1, 2]
# 3. '+' : pop 두번 -> '2', '1'을 계산 후 -> 스택에 push => stack = [3]
# 4. '3' : 스택에 push => stack = [3, 3]
# 5. '*' : pop 두번 -> '3', '3'을 계산 후 -> 스택에 push => stack = [9]
# 6. '.' : 종료, stack[0] == 9 => top 을 반환 ( stack[0] = top)

def get_caculate(arr):
    stack = []
    for i in arr[:-1]:   # 마지막 '.' 제외하고 순회
        if i.isdecimal():   # 숫자면
            stack.append(int(i))
        elif i in {'+', '-', '*', '/'}: # 연산자면
            if len(stack) < 2:  # 계산하기 전에 숫자가 2개보다 적으면 계산 불가능
                return 'error'
            b = stack.pop()
            a = stack.pop()
            if i == '+': stack.append(a+b)
            if i == '-': stack.append(a-b)
            if i == '*': stack.append(a*b)
            if i == '/': stack.append(a//b)

    if len(stack) != 1: return 'error'  # 결과값은 stack에 한개만 있어야 함
    return stack[0] #top 반환

T = int(input())
for tc in range(1, T+1):
    Forth = input().split()
    result = get_caculate(Forth)
    print(f'#{tc} {result}')