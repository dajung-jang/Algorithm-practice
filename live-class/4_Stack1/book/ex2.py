'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''

txt = input()

top = -1
stack = [0] * 100

ans = 1
for x in txt:
    if x == '(':    # 여는 괄호면 push
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호면 꺼내서 확인
        if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 ) / 스택이 비어있으면 오류(여는 괄호 부족)
            ans = 0
            break   # for x
        else:           # 짝이 맞는지 확인하기
            top -= 1    # pop
if top != -1:   # 여는 괄호가 남아있으면
    ans = 0

print(ans)
