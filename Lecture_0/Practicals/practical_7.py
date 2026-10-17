#Practical 7: Scope

#create a global variable called course_name. Define a function that prints it. Then create a local variable inside another function and explain why it cannot normally be accessed outside that function.

course_name = "Python Programming"

def show_course():
	print("Course name: ", course_name)

show_course()


def student_info():
	student_name = "Ali"
	print("Student Name:", student_name)


