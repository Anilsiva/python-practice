# Find out the gmail accounts
empty_list = []
email_list = ["exapmle1@gmail.com", "exapmle2@yahoo.com","exapmle3@outlook.com","exapmle4@hotmail.com"]
for i in email_list:
    if i.endswith("@gmail.com"):
        empty_list.append(i)
print(empty_list)

# String Comprehension
result = [i for i in email_list if i.endswith("@outlook.com")]
print(result)

# You are given a string sentence . Print the characters at even indices.
sentence = "Python is amazing"
for i in sentence:
    char_1 = sentence[0:17:2]
print(char_1)

# You are given a string s . Replace all spaces in the string with underscores ( _ ) and print the modified string.
s = "Python is fun and powerful"
for i in s:
    char_2 = s.split(" ")
    new_string = "_".join(char_2)
print(new_string)

# You are given a string s . Check if the string contains only digits.
s = "12345"
char_3 = s.isnumeric()
print(char_3)

# You are given a string s . Print the string in reverse order.
s = "Python is amazing"
char_string_1 = s[::-1]
print(char_string_1)

#You are given a string s . Capitalize the first letter of each word in the string and print the modified string.
s = "python programming is fun"
char_string_2 = s.split(" ")
new_words = []
for i in char_string_2:
    new_string_1 = i.capitalize()
    new_words.append(new_string_1)
print(" ".join(new_words))

# Title method
s = "python programming is fun"
print(s.title())

