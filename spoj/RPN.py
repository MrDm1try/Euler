priorities = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2, '(': -1}
stack = []

n = int(input())
for i in range(n):
    expr = input()
    rpn = []
    for c in expr:
        if c == ')':
            while stack[-1] != '(':
                rpn.append(stack.pop())
            stack.pop()
        elif c == '^':
            while stack and priorities[c] < priorities[stack[-1]]:
                rpn.append(stack.pop())
            stack.append(c)
        elif c in ['+', '-', '*', '/']:
            while stack and priorities[c] <= priorities[stack[-1]]:
                rpn.append(stack.pop())
            stack.append(c)
        elif c == '(':
            stack.append(c)
        else:
            rpn.append(c)
    rpn.extend(stack[::-1])
    for i in rpn:
        print(i, end='')
    print()
