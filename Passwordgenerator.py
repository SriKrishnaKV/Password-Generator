import random
import string

def password_generation():

    print("RANDOM PASSWORD GENERATOR")

    try:
        length = int(input("Enter password length: "))

        if length <= 7:
            print("Password should be minimum of 8 characters.")
            return

        print("\nSelect character types: \n1. Letters \n2. Numbers \n3. Symbols \n4. Letters + Numbers \n5. Letters + Numbers + Symbols")
      
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            characters = string.ascii_letters
        elif choice == "2":
            characters = string.digits
        elif choice == "3":
            characters = string.punctuation
        elif choice == "4":
            characters = string.ascii_letters + string.digits
        elif choice == "5":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid choice.")
            return

        password = ""
        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

    except ValueError:
        print("Please enter a valid number.")

while True:
    password_generation()

    again = input("\nDo you want to generate another password? (yes/no): ").lower()
    if again != "yes":
        print("\nThank you for using Password Generator.")
        break
