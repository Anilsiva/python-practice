'''Write a Python function square_all(numbers) that takes a list of numbers as input and 
returns a new list containing the square of each number in the input list. Use the map() 
function with a lambda function to implement this.'''
list_1 = [1,3,2,35,45,68,57,6]
square_all = map(lambda a:a**2,list_1)
print(list(square_all))

'''Write a Python function filter_positive(numbers) that takes a list of numbers as input 
and returns a new list containing only the positive numbers from the input list. Use the
filter() function with a lambda function to implement this.'''
list_1 = [1,3,2,35,45,68,57,6]
filter_positive_numbers = filter(lambda a:a%2==0,list_1)
print(list(filter_positive_numbers))

'''Write a Python function calculate_factorial(n) that calculates the factorial of a 
given number n. Use the reduce() function with an appropriate lambda function to 
implement this.'''
from functools import reduce
def calculate_factorial(n):
    return reduce(lambda a,b:a*b,range(1,n+1))
print(calculate_factorial(57))

'''Write a Python function count_vowels(string) that takes a string as input and returns 
the count of vowels (a, e, i, o, u) in the input string. Use the reduce() function with an 
appropriate lambda function to implement this.'''
from functools import reduce
def count_vowels(string):
    return reduce(lambda count, char:count+(char.lower() in "aeiou"),string,0)
print(count_vowels("Anilprasad"))