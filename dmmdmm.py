def divide(a, b):
    try:
        result = a / b
        print("Result is", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("Cleaning up and completing")
res = divide(10, 0)
print(res)