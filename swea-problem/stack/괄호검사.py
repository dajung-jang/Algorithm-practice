# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {()}는 제대로 된 짝이지만, {(})는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print('{') 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

pair = {')': '(', '}': '{'}
T = int(input())

for i in range(1, T+1):
    text = input()
    stack = []
    result = 0

    for char in text:
        if char in '{(':
            stack.append(char)
        elif char in '})':
            if len(stack) == 0:
                result = 0
                break
            elif stack[-1] == pair[char]: stack.pop()
            else:
                result = 0
                break

    # for - else 에서 else 는 for 문을 중간에 break 안걸리고 다 통과했을때만 실행되는 블록 (python에만 있음)
    else:
        if len(stack) == 0: result = 1
        else: result = 0

    print(f'#{i} {result}')

# ============= 강사님 풀이 ===============

T = int(input())

for tc in range(i, T + 1):
    text = input()
    stack = []  # 빈스택
    for i in text:
        # 여는 괄호면 무조건 스택에 추가 append
        if i == '{' or i == '(': stack.append(i)
        # 닫는 괄호가 중괄호면 짝이 맞는지 확인하고 pop
        elif stack and i == '}' and stack[-1] == '{': stack.pop()
        # 닫는 괄호가 소괄호면 짝이 맞는지 확인하고 pop
        elif stack and i == ')' and stack[-1] == '(': stack.pop()
        # 닫는 괄호가 나왔는데 짝이 맞지 않는 경우 -> 스택에 추가 append (판별할때 이게 잘못된 케이스여서 result=0 으로 돼야하는데 만약 append 안하면 결과 판별때 stack에 아무것도 안넣어져있으니 result=1로 될 수 있음 => 설정 오류
        # 여기서 append를 하지 않고 그냥 result =1 하고 break를 걸어도 될듯?
        elif i == ')' or i == '}': stack.append(i)

    # stack 이 비어 있지 않으면
    if stack: result = 0
    else: result = 1

    print(f'#{tc} {result}')

