import sys

def main():
    # sys.argv[0] is the script name, [1:] are the inputs
    args = sys.argv[1:]
    
    if not args:
        print("Usage: python calc.py <number1> <operator> <number2>")
        print("Example: python calc.py 10 + 5")
        sys.exit(1)

    # Join arguments into a single string (e.g., ['10', '+', '5'] -> "10+5")
    expression = "".join(args)

    try:
        # Evaluate the math string
        result = eval(expression)
        print(f"CALCULATION: {expression}")
        print(f"RESULT: {result}")
        sys.exit(0) # Success for Jenkins
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        sys.exit(1) # Failure for Jenkins
    except Exception as e:
        print(f"Error: Invalid math expression ({e})")
        sys.exit(1) # Failure for Jenkins

if __name__ == "__main__":
    main()
