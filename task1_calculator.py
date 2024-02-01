def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = add(num1, num2)
    operation = '+'
elif choice == '2':
    result = subtract(num1, num2)
    operation = '-'
elif choice == '3':
    result = multiply(num1, num2)
    operation = '*'
elif choice == '4':
    result = divide(num1, num2)
    operation = '/'
else:
    print("Invalid choice.")
    exit()

print(f"{num1} {operation} {num2} = {result}")
