"""
projekt_1.py: První projekt do Engeto Online Python Akademie

author: Zuzana Jurtíková
email: jurtikova.z@gmail.com
discord: susique
"""

from task_template import TEXTS

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

line = "-" * 45
print("$ python projekt1.py")

# vyžádá si od uživatele přihlašovací jméno a heslo
user = input("Username:")
password = input("Password:")
print(line)


# pokud je registrovaný, pozdrav a umožni mu analyzovat texty
if user in users and password == users[user]:
    print(f"Welcome, {user}!")
    print("We have 3 texts to be analyzed.")
    print(line)
else:
    print("Unregistered user, terminating the program!")
    print(line)
    quit()

# uživatel si vybere mezi texty uloženými v proměnné TEXTS:
number_of_texts = len(TEXTS)
selected_number = input(f"Enter a number from 1 to {number_of_texts} to select: ")
print(line)

# pokud zadá jiný vstup než číslo, program jej upozorní a skončí
if not selected_number.isnumeric():
    print("Invalid character, terminating the program!")
    print(line)
    quit()
# pokud zadá jiné číslo textu, program jej upozorní a skončí
elif int(selected_number) <= 0 or (int(selected_number) 
                                   > number_of_texts):
    print("Wrong number of text, terminating the program!")
    print(line)
    quit()
else: 
    selected_text = TEXTS[int(selected_number) - 1]
    print(selected_text)
    print(line)

# zjistí počet slov v textu
cleaned_words = []
for word in selected_text.split():
    clean_word = word.strip("!?.,:;_")
    cleaned_words.append(clean_word)

print(f"There are {len(cleaned_words)} words in the selected text.")

# počet slov začínajících velkým písmem
title_words = []
for word in cleaned_words:
    if word.istitle():
        title_words.append(word)

print(f"There are {len(title_words)} titlecase words.")

# počet slov psaných velkým písmem
upper_words = []
for word in cleaned_words:
    if word.isupper() and word.isalpha():
        upper_words.append(word)

print(f"There are {len(upper_words)} uppercase words.")

# počet slov psaných malým písmem
lower_words = []
for word in cleaned_words:
    if word.islower():
        lower_words.append(word)

print(f"There are {len(lower_words)} lowercase words.")

# počet číselných stringů a suma všech čísel (ne cifer) v textu
numeric_words = []
sum_of_numbers = 0
for word in cleaned_words:
    if word.isnumeric():
        numeric_words.append(word)
        sum_of_numbers += int(word)

print(f"There are {len(numeric_words)} numeric strings.")
print(f"The sum of all numbers is {sum_of_numbers}.")
print(line)


# graf četnosti různých délek slov
print(f"LEN|    OCCURENCES    |NR.")
print(line)
word_lenght = {}
for word in cleaned_words:
    if (len(word)) not in word_lenght:
        word_lenght[len(word)] = 1
    else:
        word_lenght[len(word)] = word_lenght[len(word)] + 1

max_length = max(word_lenght.keys())

for number in range(1, max_length + 1):
    if number in word_lenght:
        bar = '*' * word_lenght[number]
        print(f"{number:3d}|{bar: <18}|{word_lenght[number]}")
print(line)


