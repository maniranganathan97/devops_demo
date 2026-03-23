def calculator():
    print("--- Python Terminal Calculator ---")
    print("Enter 'quit' to exit.")

    while True:
        # Get user input
        user_input = input("\nEnter math (e.g., 2 + 2) or 'quit': ").strip().lower()

        if user_input == 'quit':
            print("Goodbye!")
            break

        try:
            # eval() processes the string as a math equation
            result = eval(user_input)
            print(f"Result: {result}")
        except ZeroDivisionError:
            print("Error: You can't divide by zero!")
        except Exception:
            print("Error: Invalid input. Please use numbers and +, -, *, /")

if __name__ == "__main__":
    calculator()
