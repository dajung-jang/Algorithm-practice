# 스택 : 후입선출 (나중에 들어온게 먼저 나간다)
#  => pop() 사용

def push(stack, item):
    stack.append(item)

# pop()이라는 메서드(키워드)가 있으니까 pop 이라는 명칭 사용하면 안됨
def pop_stack(stack):
    # 스택이 비어있지 않다면
    if stack: return stack.pop()
    # 스택이 비어있으면 (함수에서는 else 안씀)
    return None

# 빈스택
stack = []

push(stack, 1)
push(stack, 2)
push(stack, 3)

print(stack)

a = pop_stack(stack)
b = pop_stack(stack)
c = pop_stack(stack)

print(a)
print(b)
print(c)
print(stack)

# =========== 괄호 검사 =============

def is_brackets(text):
    stack = []

    # 괄호 순회
    for char in text:
        if char == '(': stack.append(char)  # 열린 괄호면 스택에 추가
        elif char == ')':   # 닫힌 괄호가 나왔는데
            if not stack: return False   # 스택이 비어있다면=> 실패
            stack.pop()

    # 아무 문제 없이 정상적으로 위에 로직이 동작
    return len(stack) == 0  # stack 이 비어 있다면 성공, 안 비어 있으면 실패

arr = [
    '()()((()))',
    '((()(((()()((()()())))'
]

for text in arr:
    if is_brackets(text): print(f'{text}는 올바른 괄호식 입니다.')
    else: print(f'{text}는 올바른 괄호식이 아닙니다.')

# =========== 재귀 호출 =============
# 함수 특징
# 1. 값만 복사
# 2. 함수 끝나면 해당 함수 호출했던 곳으로 돌아온다

def KFC(x):
    print(x)
    x += 1
    BTS(x + 5)
    print(x)

def BTS(x):
    print(x)

x = 3
KFC(x + 5)
print(x)

# 출력 결과는?
# 8 14 9 3

# -------------------------
def KFC(x):
    if x == 2:  # => 기저 조건 (if ~ return) (= 종료조건 이라고도 함)
        return
    print(x)
    KFC(x + 1)  # 재귀호출
    print(x)

KFC(0)

# ------------------------
def KFC(x):
    if x == 3:  # 3: level (몇 단으로 되어있는지)
        return
    KFC(x+1)    # branch : 4 (한 기준점에서 몇개의 가지가 펼쳐지는지)
    KFC(x+1)
    KFC(x+1)
    KFC(x+1)

KFC(0)

# 그래서 x 대신 lev 많이 씀 (level)
# 위 코드를 가독성 좋게 다시 쓴 코드
def KFC(lev):
    if lev == 3:        # 3: level
        return
    for i in range(4):  # 4: branch
        KFC(lev + 1)

KFC(0)

# =========== 순열 =============
# 순열 : 순서를 고려하여 나열한 것 (중복 허용 X)
#       같은 카드를 여러번 뽑을 수 없음 -> 중복 취급하지 않음

# 카드 : 0 1 2

# ex. 2장 뽑아서 순열
# 0 1       => 0 1 과 1 0 은 다른 것임
# 0 2
# 1 0
# 1 2
# 2 0
# 2 1

# =========== 중복 순열 =============
# 재귀호출 + stack
# 재귀호출 + path 배열(흔적 배열)

# ex. 2장 뽑아서 중복 순열 => 중복 순열은 중복을 허용
# 0 0
# 0 1
# 0 2
# 1 0
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

# 지금까지 뽑은 카드들을 담아놓는 바구니 (카드 두장 뽑는다고 했으니까 max len 은 무조건 2임 그 이상 되면 안됨)
path = []

def KFC(lev):
    if lev == 2:    # level:2, 2장 뽑는다 (이때 아래 코드 실행해서 path 안에 2장이 쌓여있을테니 print 하는것)
        print(*path)
        return

    for i in range(3):  #branch: 3, 카드 종류가 3종류
        path.append(i)
        KFC(lev + 1)
        path.pop()

KFC(0)

# => 재귀호출 하기 직전에 append()
#    함수가 종료되면 pop()