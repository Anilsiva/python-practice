# 1.) Concatenate two strings and print the result.
employee_name = input("enter name of the employee: ")
employee_dept = input("enter the dept of employee: ")
result = employee_name + employee_dept
print ("Combined the strings: ", result)

# 2.) Create a program that takes user age = “35”, converts it to an integer, and then prints the result type.
user_age = "35"
print(int(user_age))

# 3.) Determine the data type of a variable
discount = 58
print (type(discount))

# 4.) Display the memory addresses
employee_id = 10
person_age = 10
print (id(employee_id))
print (id(person_age))

# 5.) Create variables of different data types(int,float,str) and print their values
student_id = 1875 # integer value of student_id
student_gpa = 7.85 # float value of student_gpa
student_name = "Anil" # string value of student_name
print (student_id, student_gpa, student_name)
print (type(student_name), type(student_gpa), type(student_id))

# 6.) Create a Python script for a simple task and add comments to explain each step.
base_tri = 10 # base of the triangle
height_tri = 20 # height of the triangle
area_tri = 0.5 * base_tri * height_tri # area of the triangle
print ("Area of the triangle is: ", area_tri) 

# 7.) Write a program that prints a pattern using multiple print statements.
print ("Pattern: ")
print ("  * ")
print (" *** ")
print ("*****")
print ("  * ")

# 8.) Declare two variables, one storing an integer and the other a string. Print their values.
employee_id = 1875 # integer value of employee_id
employee_name = "SureshYadav" # string value of employee_name
print (employee_id, type(employee_id), id(employee_id))
print (employee_name, type(employee_name), id(employee_name))

# 9.) Create a Python script with both single-line and multi-line comments explaining the purpose of the script
# Print date and time along with name
import datetime
print (datetime.datetime.now())
print ("Anilprasad")

# Print the multiplication of two numbers
num_1 = 52
num_2 = 87
result = num_1 * num_2
print ("Multiplication of num_1 & num_2:", result)

'''
Above code is used to execute the result of the multiplication of two numbers
num_1 is the variable to store the value of 52 and num_2 is the variable to store
the value of 87. And the multiplication of above two variables was stored in result variable.
Finally, print the result.
'''
