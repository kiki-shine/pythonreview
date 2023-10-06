# Set of students
students = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank"}

# Set of available subjects (courses)
math_courses = {"Math 101", "Math 201", "Math 301","Math 401"}
science_courses = {"Physics 101", "Chemistry 101", "Biology 101"," Chemistry 201"}
computer_courses = {"Programming 101", "Web Development", "Data Structures"}

# Alice and Bob are enrolled in Math courses
alice_courses = {"Math 101", "Math 201"}
bob_courses = {"Math 201", "Math 301"}

# Charlie is enrolled in science courses
charlie_courses = {"Physics 101", "Chemistry 101", "Biology 101"}

# David is enrolled in both math and computer courses
david_courses = {"Math 201", "Programming 101"}

# Eve is enrolled in biology and computer courses
eve_courses = {"Biology 101", "Web Development"}

# Frank is enrolled in physics and data structures
frank_courses = {"Physics 101", "Data Structures"}
all_courses=alice_courses|bob_courses|charlie_courses|david_courses|eve_courses|frank_courses
print("The list of all enrolled courses is",all_courses)
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
science_and_math=(alice_courses|bob_courses)&charlie_courses
print("students in both science and mathematics",science_and_math)
print("..............................")
Difference1=students-(david_courses&frank_courses)
print("students not in computer science",Difference1)
new1=all_courses-(eve_courses^frank_courses)
print(new1)
new2=students.issubset(all_courses)
print(new2)
new3=alice_courses&bob_courses&david_courses
print(new3)
unique_courses=math_courses|computer_courses|science_courses 
Difference2=unique_courses-(all_courses)
print("Not enrolled courses are", Difference2)
