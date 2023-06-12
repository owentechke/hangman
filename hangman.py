# Hangman Game
# Requires words or phrases in a text file

import random
import string 
all_letters = list(string.ascii_uppercase)

guess_list = []

my_number = random.randint(1,4)

# I had multiple files, so I would choose one at random.
if my_number == 1:
    my_file = 'english2.txt'
elif my_number == 2:
    my_file = 'english3.txt'
elif my_number == 3:
    my_file = 'hangwords.txt'
elif my_number == 4:
    my_file = 'wordlist.txt'

try:
    with open(my_file) as f:
        for line in f:
            guess_list.append(line.strip())
except FileNotFoundError:
    print("File not found")

answer = random.choice(guess_list)

found_letters = ""
solution = "-"*len(answer)

counter = 0
while solution != answer:
    print (solution)
    solution=""
    print()
    print(all_letters)
    
    guess = input("What is your guess? ")
    for letter in answer:
        if letter == guess or letter in found_letters:
            solution += letter
            found_letters += letter
        else:
            solution += "-"
            
    all_letters.remove(guess.upper())
    
    counter += 1
print ("Yes! The answer is", solution, "You got it in",counter,"attempts.")