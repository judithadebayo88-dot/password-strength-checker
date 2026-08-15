import getpass

password = getpass.getpass("Enter your password: ")

# Check the password length
length = len(password)

# Check for different types of characters
has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

# Count the requirements the password meets
score = 0

if length >= 8:
    score = score + 1

if has_uppercase:
    score = score + 1

if has_number:
    score = score + 1

if has_symbol:
    score = score + 1

# Decide the password strength
if score <= 1:
    print("Password strength: WEAK")

elif score <= 3:
    print("Password strength: MEDIUM")

else:
    print("Password strength: STRONG")
