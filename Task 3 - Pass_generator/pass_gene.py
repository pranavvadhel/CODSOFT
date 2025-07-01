import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    return ''.join(random.choice(characters) for _ in range(length))

def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Please enter 'y' or 'n'.")

def main():
    print("🔐 Welcome to the Secure Password Generator!\n")

    while True:
        while True:
            try:
                length = int(input("Enter password length: "))
                if length <= 0:
                    print("❗ Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("❗ Invalid input. Enter a valid number.")

        use_upper = get_yes_no("Include uppercase letters? (y/n): ")
        use_lower = get_yes_no("Include lowercase letters? (y/n): ")
        use_digits = get_yes_no("Include numbers? (y/n): ")
        use_symbols = get_yes_no("Include symbols? (y/n): ")

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print("\n🧾 Your Generated Password:")
        print(f"👉 {password}")

        another = get_yes_no("\nGenerate another password? (y/n): ")
        if not another:
            print("\n🔒 Thank you for using the Password Generator!")
            break

if __name__ == "__main__":
    main()
