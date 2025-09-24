"""This program will check if the password entered meets the requirement """

def main():
    min_length = 8  # minimum password length
    password = input("Enter a password: ")

    # Keep asking until the password meets the minimum length
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter a password: ")

    # Print asterisks equal to the length of the password
    print("*" * len(password))


main()
