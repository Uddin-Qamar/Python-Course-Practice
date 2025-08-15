# boolean values examples
is_male = True
is_tall = False
if is_male and is_tall:
    print("you are a male, and you are tall from the list of people")
elif not (is_male) and is_tall:
    print("you are not male and you are tall")
elif is_male and not (is_tall):
    print("you are a male and you are not tall")
else:
    print("you are not a male and you are not tall at all ")

# if statements and comaprision

a = 200
b = 200
c = 200

if a > c and b > c:
    print("c is the smallest elements")
elif a > b and c > b:
    print("b is the smallest elements")
elif b > a and c > a:
    print("a is the smallest elements")
else:
    print("the program is failed to find the minimum number from the list")

    # maximum number from user through the input function
    num1 = input("enter first number")
    num2 = input("enter second number")
    num3 = input("enter the last or third number")
    if num1 > num2 and num1 > num3:
        print(num1 + "is the maximum number and it is first number")
    elif num2 > num1 and num2 > num3:
        print(num2 + " is the maximum number and its the second number from the list")
    else:
        print(num3 + " is the maximum number from the lsit , and its the third number from the given list")


# function to find the maximum number from the list
def max_num(nm1, nm2, nm3):
    if nm1 > nm2 and nm1 > nm3:
        return nm1
    elif nm2 > nm1 and nm2 > nm3:
        return nm2
    else:
        return nm3


print(max_num(333,54,1))
