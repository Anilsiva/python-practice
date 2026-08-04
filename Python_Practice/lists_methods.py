# Code for list of Squares - List comprehension
result = [i**2 for i in range(1,12)]
print(result)

# Code for list of Even numbers - List comprehension
even_numbers = [i for i in range(1,12) if i%2==0]
print(even_numbers)

# Code for remove the number 1 and it's duplicates in the given list
numbers = [3,1,4,5,2,1,6,1,9,8,1,1,1,1,1,1]
empty_list = []
for i in numbers:
    if i!=1:
        empty_list.append(i)
print (empty_list)

# Write the above code in list comprehension
numbers = [3,1,4,5,2,1,6,1,9,8,1,1,1,1,1,1]
duplicates = [i for i in numbers if i!=1]
print(duplicates)

# Print the index values from the given variable
numbers = [3,1,4,5,2,1,6,1,9,8,1,1,1,1,1,1]
empty_list = []
for i in numbers:
    if i==1:
        result = numbers.title(1)
        empty_list.append(result)
print(empty_list)
 