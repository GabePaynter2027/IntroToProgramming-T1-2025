def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Welcome to the Simple Calculator!")

x = input("Enter the first number (x): ")
y = input("Enter the second number (y): ")


x = int(x)
y = int(y)

print("Choose the operation you want to perform:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

choice = input("Enter the number of the operation (1/2/3/4): ")

operations = {
    "1": add,
    "2": subtract,
    "3": multiply,
    "4": divide
}

def invalid_choice(x, y):
    return "Invalid choice."

operation_function = operations.get(choice, invalid_choice)
result = operation_function(x, y)

print("Result:", result)