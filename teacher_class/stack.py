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

