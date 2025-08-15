#file reading in python
"""
file_1 = open("one.txt", "r")
print(file_1.readable())
print(file_1.read())
file_1.close()
"""
# appending to a file in python (add some text at the end of existing files)
"""
file_2 = open("one.txt", "a")
file_2.write("\n Now the questions is looking wonderfull.")
file_2.write("\n The questions clarifiy the answers of the attandee. ")
file_2.close()
"""
# write a file in python *(it used to write a new file or overwrite the existing file)

file_3 = open("one.txt1", "w")
file_3.write("Hi Qamar,\nI am here , whats about you.")

# to create a new file
file_4 = open("one.txt1", "w")
file_4.write("Hi Robot,\nI am here for your help.\n Do you need any help.?")

