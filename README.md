# 🔐 Python Password Generator

A simple and secure password generator written in Python.  
Generates strong, random passwords with a customizable length and includes uppercase, lowercase, numbers, and symbols.

---

## 🚀 Features

- Customizable password length
- Uses uppercase, lowercase, digits, and punctuation
- Lightweight and fast
- Uses only Python's standard libraries
- Great for learning or personal use

---

## 📦 Requirements

- Python 3.x  
- No external libraries required

---

## 🧪 How to Use

1. Run the script:

python password_generator.py
Follow the prompts:

Enter password length (e.g., 16)

Choose whether to include symbols (e.g., y for yes, n for no)

Choose whether to save the password to a file (saved as generated_password.txt)

---
##🧾 Example Output:

Enter password length: 12
Include symbols? (y/n): y
Generated password: 9g@D#2bLx!f1
Save password to file? (y/n): y
[✓] Password saved to generated_password.txt
The file will be created in the same folder where the script is located.

---
##📌 Planned Updates:

🔐 1. Secure password storage
Instead of saving to plain .txt, encrypt passwords using:

cryptography or PyNaCl library

Option to set a master password
✅ 2. Password strength estimator
Give a rating (Weak / Medium / Strong) based on:

Length

Variety of characters used

Entropy estimation

---
##⚠️ Disclaimer
This script is for educational and personal use only.
Do not use this to manage or store real passwords without additional security measures (e.g., encryption, secure storage).

---
