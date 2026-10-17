#Practical 7B: Scope

#create a global variable called course_name. Define a function that prints it. Then create a local variable inside another function and explain why it cannot normally be accessed outside that function.

def student_info():
	student_name = "Ali"
	print("Student Name:", student_name)
student_name  


#Variable scope problem

#student_name is created inside the function student_info().

#When you write student_name outside the function, Python cannot find it and raises:
# NameError: name 'student_name' is not defined