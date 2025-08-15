# advanced level of calculator to perform various operation
num1 = float(input("enter the first number :"))
op = input("Please enter your desired operator :")
num2 = float(input("enter the second number :"))
if op == "+" :
    print(num1 + num2 )
    print("the operation is of subtraction")
elif op == "-":
    print(num1-num1)
    print("the operation is of subtraction")
elif op == "*":
    print(num1 * num2)
    print("the operation is of multiplication")
elif op == "/":
    print(num1/num2)
    print("the operation is of division")
elif op == "%":
    print(num1%num2)
    print("the operation is of modulous and it gives the reminder of the two number")
else:
    print("invalid operator")



