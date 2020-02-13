#list
students = ["leroy", "julius", "collins"]
print(students)

# create an empty list
students = []
print (students)

# indexing the list
students = ["leroy", "julius", "collins", "samuel", "omar", "gabriel"]
print (students[1]) #diplay index 1 from the list
print (students[0])#diplay index 0 from the list
print (students[2:5])#diplay index 2:5 from the list
print (students[2:])#diplay index 2: from the list
print (students[:5])#diplay index :5 from the list

#indexing replacing
students [3] = "stephanie" #replacing "samuel" with " stephanie"
students [4] = "george" #replacing " omar" with "george"
print (students) #display the replacing

#loop through the list
for student in students:
  print (student) #display the loop

#check if item exists
if "stephanie" in students:
  print ("stephanie is there") #diplay "stephanie" is there
  print ("mark is not there") #display "mark is not there"

  #methods
#len(), append(), insert(), pop()
print(len(students))
students.append("collins") #appended "collins" into list
print (students)
students.insert(3, "grace") #inserted "grace"to position 3
print (students)
students.pop(1) #removes name located under (1) on list
print (students)
students.remove("george") #removes "george" from list
print (students)
students.reverse() #reverses list from first to last
print (students)
students.sort() #sorts list in alphabetical order
print (students)
students. clear() #clears whole list of students
print (students)