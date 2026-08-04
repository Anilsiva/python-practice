# Generate multiplication of tables in sequence
'''number = int(input("Enter the multiplication number:"))
for i in range(1,11):
    result = number * i
    print (f"{number} X {i} = {result}")
print ("-"*25)'''

# Generate multiplication of tables using nested for loop
'''for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print(f"{i} X {j} = {result}")
    print ("-"*25)'''

# Generate 10 times usernames and the loop will stopped when username equals to stop.
'''while True:
    user_name = input("Enter the username:")
    print(f"The username is {user_name}")
    if user_name == "stop":
        break'''

# Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop.
empty_list = []
for i in range(1,6):
    result = i**2
    empty_list.append(result)
print(empty_list)
print(f"Sum of squares:", sum(empty_list))

#Write a Python program that uses a while loop to print a countdown from 5 to 1.
count = 5
while count >= 1:
    print(count)
    count -= 1

# Write a Python program to print the multiplication table for a user-specified number using a nested for loop. 
for i in range(1,11):
    for j in range(1,11):
        multiplication = i * j
        print(f"{i} X {j} = {multiplication}")
    print("-"*25)

# Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive).
for i in range(11):
    for j in range(11):
        if i%2==0:
           sum = i + j
print(f"Sum of all even numbers is {sum}")

# Calculate the sum of all numbers from 1 to a given number
num_1 = int(input("Enter the number:"))
for i in range(1,num_1+1):
    for j in range(1,num_1):
        i = i+j
print(f"Sum of all numbers is {i}")

#Display numbers from a list using loop
sample_list = []
for i in range(10):
    sample_list.append(i)
print(sample_list)

# List comprehension
list_1 = [i for i in range(10)]
print(list_1)

# Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)

# List comprehension
numbers_list = [i for i in range(-10,0)]
print(numbers_list)

#Write a Python program to print the cube of all numbers from 1 to a given number
sample_number = int(input("Enter the number:"))
sample_list_1 = []
for i in range(1,sample_number+1):
    cubes = i ** 3
    sample_list_1.append(cubes)
print(sample_list_1)



