import random
import string

def generate_password(length=12, use_symbols=True):
    characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename="generated_password.txt"):
    try:
        with open(filename, "w") as file:
            file.write(password + "\n")
        print(f"[✓] Password saved to {filename}")
    except IOError:
        print("[!] Failed to write to file.")

if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        symbol_choice = input("Include symbols? (y/n): ").strip().lower()
        use_symbols = symbol_choice == 'y'

        password = generate_password(length, use_symbols)
        print("Generated password:", password)

        save_choice = input("Save password to file? (y/n): ").strip().lower()
        if save_choice == 'y':
            save_password_to_file(password)

    except ValueError:
        print("[!] Invalid input. Please enter a valid number for length.")