import random
import string
print("Welcome to Password Generator!\n".center(100))

def password_generator(length,complexity):

    # Combination of letters, digits and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Conditional statements for different complexity 
    if complexity == "high":
        password=[random.choice(string.ascii_lowercase),
                  random.choice(string.digits),
                  random.choice(string.punctuation),
                  random.choice(string.ascii_uppercase)]
        
    elif complexity=="medium":
        password=[random.choice(string.ascii_letters),
        random.choice(string.digits)]

    else:
        password=[random.choice(string.ascii_letters)]


    #Random choice of the characters and passwords
    while len(password) < length:
        random_char = random.choice(characters)
        if random_char not in password:
            password.append(random_char)

    return "".join(password)

# Taking inputs from the user
while True:
    try:
        length=int(input("Enter the length of the password (mimimum 5 characters): "))
        if length<5:
            print("Password must be at least 5 characters")
            continue
        else:
            break
    except ValueError:
        print("Enter the length of the password")
        continue
while True:
    try:
        complexity=input("Enter the complexity level\n1.High\n2.Medium\n3.Low\n").strip().lower()
        break
    except ValueError:
        print("Enter a valid complexity")
        continue

print(password_generator(length,complexity))
