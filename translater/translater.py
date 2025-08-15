# the translater used to convert the the space of wovel into s

def transalater (pharase):
  translation = ""
  for letter in pharase:
    if letter in "AEIOUaeiou":
      translation = translation + "s"
    else:
      translation = translation + letter
  return translation

print(transalater(input("enter pharase")))

# error exceptin commond
try:
 number = int(input("enter a number"))
 print(number)
except:
 print("invlaid values")









