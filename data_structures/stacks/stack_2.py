from stacks import Stack


def evaluate_postfix(expression):
    stack = Stack()
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.push(int(token))
        else:
            if stack.size() < 2:
                raise ValueError("Invalid postfix expression")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = evaluate_operator(token, operand1, operand2)
            stack.push(result)

    if stack.size() != 1:
        raise ValueError("Invalid postfix expression")
    return stack.pop()

def evaluate_operator(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    else:
        raise ValueError(f"Unknown operator: {operator}")

