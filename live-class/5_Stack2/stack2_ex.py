icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

stack = [0]*100
top = -1
fx = '(6+5*(2-8)/2)'
susik = ''

for x in fx:
    if x not in '(+-*/)':   # 피연산자인 경우 출력
        susik += x
    elif x == ')':  # 여는 괄호까지 pop
        while stack[top] != '(':    # peek
            top -= 1
            susik += stack[top + 1]
        top -= 1    # 남이있는 '(' 버림
    else:   # 연산자인 경우
        if top == -1 or icp[x] > isp[stack[top]]:   # icp > top 원소 isp : push
            top += 1
            stack[top] = x
        else:    # icp <= isp : icp > isp 까지 pop
            while top > -1 and isp[stack[top]] >= icp[x]:
                top -= 1
                susik += stack[top+1]
            top += 1    # push x
            stack[top] = x

print(susik)