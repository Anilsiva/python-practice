# Write Python code to add a new key-value pair to the following dictionary
my_dict = {'name': 'python', 'age': 25}
my_dict['city'] = 'West Godavari'
print(my_dict)

# Write Python code to access and print the value associated with the key 'price' in the following dictionary:
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
value_1 = product_info['price']
print(value_1)

# Write Python code to remove the key-value pair with the key 'city' from the following dictionary:
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict['name']='John'
my_dict.pop('city')
print(my_dict)

# Write Python code to print all the keys present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'}
dict_keys = list(my_dict.keys())
print(dict_keys)

# Write Python code to print all the values present in the following dictionary:
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
dict_values = list(my_dict.values())
print(dict_values)

# Write a Python script that updates a dictionary with a new key-value pair.
my_dict = {'name': 'python', 'age': 25}
my_dict['city'] = 'East Godavari'
print(my_dict)

# Write a Python script that accesses and prints the value associated with a specific key in a dictionary.
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
for i in my_dict.items():
    print(i)

# Write a Python script that removes a key-value pair from a dictionary.
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
my_dict.clear()
print(my_dict)

# Write a Python script that prints all the keys present in a dictionary
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
dict_keys_1 = list(my_dict.keys())
print(dict_keys_1)

# Write a Python script that prints all the values present in a dictionary
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
dict_values_1 = list(my_dict.values())
print(dict_values_1)


'''Create a program that manages a dictionary of word meanings. The program
should allow users to perform the following actions:
1. Add a Word: Allow users to add new words along with their meanings to the
dictionary.
2. Search for Meaning: Enable users to search for the meaning of a word in the
dictionary.
3. Display All Words: Provide an option to display all words and their meanings
currently stored in the dictionary.
4. Update Meaning: Implement a feature to update the meaning of an existing
word in the dictionary. After updating, display the updated meaning.
5. Delete Word: Implement a feature to delete a word and its meaning from the
dictionary. Confirm the deletion and handle cases where the word doesn't
exist.
Ensure the program handles invalid inputs gracefully. Use a while loop to keep the
program running until the user chooses to exit.'''

dictionary = {}
while True:
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        word = input("Enter a word:")
        meaning = input("Enter the meaning:")
        dictionary[word] = meaning
        print(f"Word added successfully")

    elif choice == 2:
        word = input("Enter the word to search:").lower()
        if word in dictionary:
            print(f"The meaning is {dictionary[word]}")
        else:
            print(f"Word not found in dictionary")

    elif choice == 3:
        if dictionary:
            for word, meaning in dictionary.items():
                print(f"{word} : {meaning}")
        else:
            print(f"Dictionary is empty")
    
    elif choice == 4:
        word = input("Enter the exising word:")
        if word in dictionary:
            new_meaning = input("Enter the new meaning:")
            dictionary[word] = new_meaning
            print(f"{word}:{new_meaning}")
            print("New meaning updated successfully")
        else:
            print(f"Word not found in dictionary")

    elif choice == 5:
        word = input("Enter the word:")
        if word in dictionary:
            dictionary.pop(word)
            print(f"The given {word} is deleted")
        else:
            print(f"Word not found in dictionary")

    elif choice == 6:
        break
        
