🔐 Caesar Cipher – Python Implementation

A simple and clean Python implementation of the classic Caesar Cipher, supporting both encryption and decryption with customizable shift values.
This project demonstrates basic string manipulation, translation tables, and user interaction in Python.

✨ Features

🔤 Encrypt any text using the Caesar Cipher

🔓 Decrypt encrypted text back to its original form

🔢 Validates shift input (must be between 1–25)

🆙 Supports both lowercase and uppercase letters

🔁 Interactive loop for multiple operations

🧩 Clean, modular functions (encrypt, decrypt, caesar)

📌 How It Works

The Caesar Cipher shifts each letter in the alphabet by a set number of positions.
Example:

Shift: 3

“ABC” → “DEF”

“xyz” → “abc”

Your program uses a translation table to quickly map letters to their shifted positions.

🧠 Code Structure
1. caesar(text, shift, encrypt=True)

Handles the main logic:

Validates the shift

Builds shifted alphabet

Creates translation table

Returns encrypted or decrypted text

2. encrypt(text, shift)

Encrypts text by calling caesar().

3. decrypt(text, shift)

Decrypts text by reversing the shift.

4. Interactive Program Loop

Asks the user to choose:

E → Encrypt

D → Decrypt

Then prints the result.
