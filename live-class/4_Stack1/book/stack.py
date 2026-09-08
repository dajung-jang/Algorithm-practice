# 간단한 스택
top = -1
stack = [0] * 10

top += 1            # push(1)
stack[top] = 1
top += 1            # push(2)
stack[top] = 2
top += 1            # push(3)
stack[top] = 3

# 함수에서는 리턴값이 마지막에 오는데 그 뒤에 top -= 1 을 할 수 었으니 위에서 하고 return에서는 top +1 하는거임
# 여기는 함수가 아니지만 나중에 함수를 쓸 때 헷갈리지 않도록 여기서도 그냥 먼저 top -= 1을 함
top -= 1            # pop()
print(stack[top+1])
top -= 1            # pop()
print(stack[top+1])
top -= 1            # pop()
print(stack[top+1])