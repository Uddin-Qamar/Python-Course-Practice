# basics knowledge of lists
subjects = ['Physis', 'chemistry', 'computer science', 'Mathimatics']
marks = [20, 58, 44, 2]
print(marks)
print(subjects)
print(subjects[1])
print(subjects[3])
print(subjects[-1])
print(subjects[-4])
print(subjects[1:2])
print(subjects[1:])
subjects[3] = "Psychology"
print(subjects)
print(marks)

# function of lists
#1. Extend function used to add or connect two or more list togather to show all elements into a single list
subjects.extend(marks)
print(subjects)
#2 append function used to add an extra elements into the end of the list
subjects.append('Math')
print(subjects)
#3 insert function is used to add a new elments into a specified location of the list
subjects.insert(2, 'Biology')
print(subjects)
# 4 remove function is used to remove/delete a single elements from the list
subjects.remove('Math')
print(subjects)
# 5 pop func is used to remove the last elements of the list and also remove the elements if its index is given
subjects.pop()   #remove last elements
print(subjects)
subjects.pop(2)  # remove the elements of index value 2
print(subjects)
subjects.insert(3,'Economics')
print(subjects)

#6 clear fuction is used to remove every elements from the list, it shows an empty list
# subjects.clear()
# 7 count function is used to print out the count of repeated elements in the list
subjects.insert(2,'computer science')
print(subjects)
print(subjects.count('computer science'))
# 8 sort function is used to sort the elements in the order
marks.sort()
print(marks)

name = ['qamar','kamran', 'mohsin','sunil','hassan','ashfaq','awais','saim']
print(name)
name.sort()
print(name)

# 9 reverse function is used to revers the order of the list elemenst
name.reverse()
print(name)
marks.reverse()
print(marks)

# 10 copy function is used to copy the elements from one list into other list
name2 = name.copy()
print(name)
print(name2)





