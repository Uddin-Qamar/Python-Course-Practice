# while loop for table of a number
i = 1
tb = 20
while i <= 10 and tb <= 200:
    resl = i*tb
    print(i,"x",tb,"=", resl)
    i += 1

print("Loop is executed succesfuly")

# for loop

for letter in "University of eastern Finland":
    print(letter)

subjects = ["Physis", "chemistry", "Math","Bio"]
for sub in subjects :
    print(sub)
for i in range(20):
    print(i)
for i in range(3,9):
    print(i)

friends = ["qamar","Taimoor","Muazzam"]
for fr in friends:
    print(fr)
else:
    print("no iteam left")
# Exponent function and operation
print(2**6)

# exponent power function

def pow_func(base_num,pow_num):
    result = 1
    for i in range(pow_num):
        result = result*base_num
        return result
print(pow_func(2,4))

# 2D list
number_lis = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(number_lis[1][2])

name_lis = [
    ["Qamar", "Said", "Khalil"],
    ["Zaheer", "Taimoor", "Muazzam"],
    ["Salaho", "Saleem", "Zia"]

]
print(name_lis[0][2])

#Nested for loop is being used to access the elements of number_lis (2D list)
#first examples of number list
for row in number_lis:
    for col in row:
        print(col)

# second example of name list
for row in name_lis:
    for col in row:
        print(col)
        









