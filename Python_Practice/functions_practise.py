# Write a Python function named add that takes two arguments a and b and returns their sum.
def add(a,b):
    return a+b
obj = add(25,17)
print(obj)

# Write a Python function named square that takes a number x as input and returns its square.
def square(x):
    return x**2
result = square(175)
print(result)

# Write a Python function named factorial that takes a positive integer n as input and returns its factorial.
import math
def factorial(n):
    return math.factorial(n)
result = factorial(87)
print(result)

# Write a Python function named maximum that takes a list of numbers as input and returns the maximum value in the list.
def maximum(m):
    return max(m)
m = [1,2,3,5]
print(maximum(m))

# Write a Python function named reverse that takes a string s as input and returns its reverse.
s = 'SwethAnil' 
def reverse(s):
    return s[::-1]
print(reverse(s))

#vWrite a Python function named is_prime that takes a positive integer n as input and returns True if n is prime, otherwise False .
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i ==0:
            return False
    return True
result = is_prime(2029)
print(result)

# Write a Python function named fibonacci that takes a positive integer n as input and returns the n th Fibonacci number.
list_1 = []
def fibonacci(n):
    a,b = 0,1
    for i in range(0,n):
        list_1.append(a)
        a,b = b,a+b
    return list_1 
print(fibonacci(4))

# Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome, otherwise False .
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome('12124'))

# Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.
n = [1,2,3]
def sum_of_squares(n):
    total = 0
    for i in n:
        total = total + (i**2)
    return total
print(sum_of_squares(n))

# Write a Python function named average that takes a list of numbers as input and returns the average value.
a = [1,2,35,75,8,5,7]
def average(a):
    total = sum(a)/len(a)
    return total
print(average(a))