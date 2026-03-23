import sys

def calculator():
    # Check if the user provided an argument (sys.argv[0] is the filename)
    if len(sys.argv) < 2:
        print("Usage: python calc.py '2 + 2'")
        sys.exit(1)

    # Join all arguments into one string (e.g., 2 + 2 becomes "2+2")
    expression = "".join(sys.argv[1:])

    try:
        result = eval(expression)
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: Invalid expression. {e}")
        sys.exit(1)

if __name__ == "__main__":
    calculator()
