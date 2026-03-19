# tuple is a type of data structure
# a tuple is a bit different from a list, it cant be changed or updated once it has been created
coordinates = (2,4,66,33,77,22,10,100)
print(coordinates)
print(coordinates[2])


#Function
# Example 1:
def say_hi():
    print("hello dear")
    x = 'Welcome to the python course'
    print(x)
    y = 5
    z = 6
    w = y +z
    print(w)
say_hi()

# Example 2:
def user_inf(name, age, city):
    print("My name is " + name +! " I am  " + str(age) + " year old, and I from " + city)
user_inf("Qamar", 27, "Helsinki")
user_inf("Zaman", 17, "Karachi")

# use of return key words.
# Example 3:

def cube(num):
    print(num)
    return num*num*num
  # after return key words python are not accepts any value inside the function
result = cube(4)
print(cube(8))
print(result)


