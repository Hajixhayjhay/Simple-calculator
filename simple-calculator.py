name = "Hajarat"
message = F"Hi {name}! Welcome to my python calculator"

print(message)

def add(x, y):
    return x + y

def subract(x, y):
    return x - y

def divide(x, y):
    return x / y
    if y == 0:
        return "Error! Cannot divide by zero"

def multiply(x, y):
    return x * y

def power(x ,y):
    return x ** y


def squareroot(x):
    return x ** 0.5


def display_menu():
    print("Python calculator")
    print("Select operation")
    print("0. exit")
    print("1. add")
    print("2. subract")
    print("3. divide")
    print("4. multiply")
    print("6. squareroot")

choice = input("Enter your choice (0/1/2/3/4/5/6): ")

if choice == '0':
    print("Thank you for using this calculator. Goodbye!")

elif choice in ['1', '2', '3', '4', '5']:
    num1 =float(input("Enter first number: "))
    num2 =float(input("Enter second number: "))

elif choice in ['6']:
    num =float(input("Enter a number: "))

else:
    print("Invalid choice. Please enter a number from 0-6")


if choice == '1':
    print("Result:", add(num1, num2))

elif choice =='2':
    print("Result:", subract(num1, num2))

elif choice == '3':
    print("Result:", divide(num1, num2))

elif choice == '4':
    print("Result:", multiply(num1, num2))

elif choice == '5':
    print("Result:", power(num1, num2))

elif choice == '6':
    print("Result:", squareroot(num))

else:
    print("Invalid choice. Please enter a number from 0-6")


