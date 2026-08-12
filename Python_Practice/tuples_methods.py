'''Create a Tuple: Write a program that creates a tuple containing three
elements: your name, your age, and your favorite color. Then print the tuple.'''
user_details = "anilprasad", 31, "Blue"
print(user_details)
print(type(user_details))

#Access Tuple Elements: Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.
days_of_the_week = "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"
print(days_of_the_week.index("Tuesday"))
for i in days_of_the_week:
    if i=="Tuesday":
        print(i)

'''Tuple Concatenation: Write a program that creates two tuples, one
containing odd numbers from 1 to 5 and another containing even numbers
from 2 to 6. Concatenate these two tuples and print the result.'''
tuple_1 = (1,3,5)
tupel_2 = (2,4,6)
tuple_3 = tuple_1 + tupel_2
print(tuple_3)

'''Tuple Unpacking: Write a program that defines a tuple containing the
dimensions of a rectangle (length and width). Then, unpack this tuple into
two variables and calculate the area of the rectangle.'''
rectangle_dimensions = (25,15)
length_rec, width_rec  = rectangle_dimensions
area_rec = length_rec * width_rec
print (area_rec)

    


