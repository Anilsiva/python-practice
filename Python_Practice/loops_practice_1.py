# Generate multiplication of tables in sequence
number = int(input("Enter the multiplication number:"))
for i in range(1,11):
    result = number * i
    print (f"{number} X {i} = {result}")
print ("-"*25)

# Generate multiplication of tables using nested for loop
for i in range(1,11):
    for j in range(1,11):
        result = i * j
        print(f"{i} X {j} = {result}")
    print ("-"*25)

# Generate 10 times usernames and the loop will stopped when username equals to stop.
while True:
    user_name = input("Enter the username:")
    print(f"The username is {user_name}")
    if user_name == "stop":
        break