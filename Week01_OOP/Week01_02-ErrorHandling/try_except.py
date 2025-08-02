def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("❌ Error: Cannot divide by zero.")
    except TypeError:
        print("❌ Error: Please enter numbers only.")
    else:
        print(f"✅ Result: {result}")
    finally:
        print("✔️ Division attempt complete.")

# Test
divide_numbers(10, 2)
divide_numbers(10, 0)
divide_numbers("10", 5)
