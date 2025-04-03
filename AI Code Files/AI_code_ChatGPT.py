"AI Assisted Coding ChatGPT Version"

def calculator():
    while True:
        try:
            expression = input("Enter a mathematical expression (e.g., 5 + 3 * 2): ").strip()
            if expression.lower() in ['exit', 'quit']:
                print("Exiting calculator.")
                break
            result = eval(expression, {"__builtins__": {}}, {})
            print(f"{expression} = {result}")
        except (SyntaxError, NameError, ZeroDivisionError):
            print("Invalid input. Please enter a valid mathematical expression.")

calculator()
