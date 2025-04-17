from postfix import evaluate_postfix

def main():
    expression = input("Enter a postfix expression: ")
    try:
        result = evaluate_postfix(expression)
        print(f"The result of the postfix expression '{expression}' is: {result}")

    except ValueError as e:
        print(f'Error: {e}')



if __name__ == "__main__":
    main()



