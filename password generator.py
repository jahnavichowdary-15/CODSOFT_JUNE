import random
import string

print("=== Password Generator ===")

# Ask the user for password length
length = int(input("Enter the desired password length: "))

# Define the characters to use
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the password
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)
