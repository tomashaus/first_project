op_list = ("+", "-", "*", "/", "//")

while True:
    num_1 = input("Enter a number: ")
    try:
        num_1 = float(num_1)
        break
    except ValueError:
        print("Not a number try again.")

while True:
    op = input("Enter an operation: ")
    if op not in op_list:
        print("Try again.")
    else:
        break

while True:
    num_2 = input("Enter a second number: ")
    try:
        num_2 = float(num_2)
        break
    except ValueError:
        print("Not a number try again.")

if op == "+":
    print(num_1 + num_2)
elif op == "-":
    print(num_1 - num_2)
elif op == "*":
    print(num_1 * num_2)
elif op == "/":
    print(num_1 / num_2)
elif op == "//":
    print(num_1 // num_2)