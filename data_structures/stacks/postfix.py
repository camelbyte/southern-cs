from stack import Stack

def evaluate_postfix(expression):
    """
    Description: This function evaluates a postfix expression using a stack.

    Params: Takes a string (expression) 

    Return: the result of the expression.
    """

    # tokens will hold the split string containing the operators and operands 
    tokens = expression.split()
    operators = {'+', '-', '*', '/'}
    stack = Stack()


    for t in tokens:
        # Use a loop to iterate throught the tokens and check if they're operators or operands
        if t not in operators:
            try:
                v = int(t)
            except ValueError:
                try:
                    v = float(t)
                except ValueError:
                    raise ValueError(f"Invalid operand: {t}")
            stack.push(v)
        else:
            # if there are enough operands in the stack, it pops them and applies the operator 
            if stack.size() < 2:
                raise Exception("Invalid postfix expression: insufficient operands.")
            # This is where the actual evaluation happens
            b, a = stack.pop(), stack.pop()
            if t == '+': res = a + b
            elif t == '-': res = a - b
            elif t == '*': res = a * b
            elif t == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero encountered.")
                res = a / b
            stack.push(res)

    if stack.size() != 1:
        raise Exception("Invalid postfix expression: too many operands remaining.")

        # Return the final result which should be 1 number
    return stack.pop()


if __name__ == "__main__":
    # Evaluating a postfix expression 
    expression = "3 5 1 - * 2 +"
    try:
        result = evaluate_postfix(expression)
        print(f"Postfix: '{expression}' is: {result}")
    except Exception as e:
        print(f"Error evaluating expression: {e}")

