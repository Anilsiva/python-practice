#Write a Python program that takes a character as input and checks whether it is a vowel or not.
char_1 = input("Enter the character:")
vowel = "aeiouAEIOU"
if char_1 in vowel:
    print ("The entered character is a Vowel")
else:
    print ("The entered character is not a Vowel")

# Write a program that takes an age as input and classifies the person
age = int(input("Enter the person age:"))
if age == 0 or age <= 12:
    print (f"The entered age is {age}, the person is a Child")
elif age >= 13 and age <= 17:
    print (f"The entered age is {age}, the person is a Teenager")
elif age >= 18 and age <= 64:
    print (f"The entered age is {age}, the person is an Adult")
else:
    print (f"The entered age is {age}, the person is Senior")

#Write a program that takes an integer as input and classifies it as positive, negative, or zero.
num_1 = int(input("Enter the number:"))
if num_1 > 0:
    print (f"The entered number {num_1} is Positive")
elif num_1 < 0:
    print (f"The entered number {num_1} is Negative")
else:
    print (f"The entered number {num_1} is Zero")

#Create a program that checks whether a given year is a leap year or not.
year = int(input("Enter the Year:"))
if year%4 == 0 or year%400 == 0:
    print (f"The entered year {year} is a Leap Year")
else:
    print (f"The entered year {year} is not a Leap Year")

# Build a simple calculator program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation.
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
print (f"The value of addition is {addition}\nThe value of subtarction is {subtraction}\nThe value of multiplication is {multiplication}\nThe value of division is {division}")

#Short Hand if
x = int(input("Enter the number:"))
result = "EVEN" if x%2==0 else "ODD"
print (result)

#Write a program that calculates the Body Mass Index (BMI)
weight = float(input("Enter the value of weight:"))
height = float(input("Enter the value of height:"))
BMI = weight / (height ** 2)
print (f"The BMI value is {BMI}")

# Create a program that calculates the final price after applying a discount.
# The program should take the original price and the discount percentage as input.
price = float(input("Enter the Product Price:"))
discount = float(input("Enter the Discount:"))
final_price = (price - (price*(discount/100)))
print (f"The Final Price of the Product after discount is {final_price}")
