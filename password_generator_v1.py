import random
import string
import itertools
import time
import os

# clearing the terminal
os.system('cls')

# making a class to animate the text
class Text:
    def __init__(self, text, sleep_time):
        self.sleep_time = sleep_time
        self.text = text
    
    def show(self):
        for char in self.text:
            print(char, end="", flush=True)
            time.sleep(self.sleep_time)


text = Text("Welcome to my Password generator and Brute force simulation!\n", 0.04)
text.show()

chars = string.ascii_lowercase

# collecting user inputs
text2 = Text("\nCreating a password:", 0.04)
text2.show()

question = Text("\nDo you want big letters in it? (y/n): ", 0.03)
question.show()
big_letters = input()

question2 = Text("Do you want numbers in it? (y/n): ", 0.03)
question2.show()
numbers = input()

question3 = Text("Do you want special signs in it? (y/n): ", 0.03)
question3.show()
special_signs = input()

question4 = Text("Length of a password? (better use 4 or less, not more than 5): ", 0.03)
question4.show()
length_of_password = int(input())

# making an array of characters to choose from for a password
if big_letters.lower() == "y":
    chars += string.ascii_uppercase
if numbers.lower() == "y":
    chars += string.digits
if special_signs.lower() == "y":
    chars += "!@#$%^&*?"

# generates a random password based on user settings
def generate_password():
    return "".join(random.choice(chars) for _ in range(length_of_password))

password = generate_password()

text3 = Text(f"\nGenerated password: {password}", 0.05)
text3.show()
text4 = Text("\nSimulating a brute-force attack...", 0.06)
text4.show()

start = time.time()
attempts = 0

# simulating a brute-force attack
for guess in itertools.product(chars, repeat=length_of_password):
    attempts += 1
    if "".join(guess) == password:
        end = time.time()
        print("\n____________________")
        print("Password was found!!")
        print(f"Attempts: {attempts}")
        print(f"Time taken: {end - start:.5f} seconds!")
        break