#Practical 3: Operators
#Ask a user to enter two numbers. Display their sum, difference, product, quotient and remainder. Test what happens when the second number is zero.

num1 = int(input("Enter first number: "))

operator = input("Enter operator (+, -, *, /): ") 

num2 = int(input("Enter second number: "))	

sum = num1 + num2

difference = num1 - num2

product = num1 * num2

if num2 !=0:

	quotient = num1 / num2

	remainder = num1 % num2

else:
	quotient = "Error: Division by zero is not allowed"

	remainder = "Error: Division by zero is not allowed"

print("Sum: ", sum)
print("Difference: ",difference)
print("Product: ",product)
print("Quotient: ",quotient)
print("Remainder: ",remainder)
