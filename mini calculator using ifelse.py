a = int(input("A: "))
b = int(input("B: "))
operator = input("choose add,sub,multiply,divide=")

if operator == "add":
    result = a + b
    print("result =", result)
elif operator == "sub":
    result = a - b
    print("result =", result)
elif operator == "multiply":
    result = a * b
    print("result =", result)
elif operator == "divide":
    if b != 0:
        result = a / b
        print("result =", result)
    else:
        print("division by zero is not allowed")
else:
    print("enter valid info")
