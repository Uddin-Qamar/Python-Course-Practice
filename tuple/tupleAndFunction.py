# tuple is a type of data structure
# a tuple is a litbit different from a list, it cant be changed or updated once it has been created
coordinates = (2,4,66,33,77,22,10,100)
print(coordinates)
print(coordinates[2])


#Function
def say_hi():
    print("hello dear")
    x = 'Welcome to the python course'
    print(x)
    y = 5
    z = 6
    w = y +z
    print(w)
say_hi()

def user_inf(name,age,city):
    print("Hello " + name + " And you are " + str(age) + " year old, and you are from " + city)
user_inf("Qamar", 27, "Helsinki")
user_inf("Zaman", 17, "Karachi")
# use of return key words.
def cube(num):
    print(num)
    return num*num*num
  # after return key words python are not accepts any value inside the function
result = cube(4)
print(cube(8))
print(result)


