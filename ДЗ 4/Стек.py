def delete(stack):
    if len(stack) % 2 == 1:
        stack.pop(len(stack) % 2 + 1)
    elif len(stack) % 2 == 0:
        stack.pop(len(stack) % 2 + 1)
        stack.pop(len(stack) % 2 + 1)
    
    return stack

stack = []

stack.append(3)
stack.append(15)
stack.append(4)
stack.append(8)
stack.append(7)

print(stack)
stack[0], stack[-1] = stack[-1], stack[0]
print(stack)
stack = delete(stack)
print(stack)
stack = delete(stack)
print(stack)