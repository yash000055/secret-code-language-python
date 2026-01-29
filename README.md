# Secret Code Language Translator using Python
This is a Python program that encodes normal English text into a secret code language and decodes it back to readable English using predefined transformation rules.

Description

The program performs encoding and decoding of text based on word length. It uses string manipulation, random character insertion, and vowel substitution to generate a secret-coded message. The decoding logic reverses the same process to retrieve the original message.

Features

Encode English text into a secret code language.

Decode secret code back into readable English.

Uses random characters for obfuscation.

Simple command-line interface.

Handles multi-word input.

Encoding Rules

For each word in the input message:

Case 1: Word length is 3 or more characters

Convert the word to lowercase.

Remove the first three characters and append them to the end of the word.

Add four random characters at the beginning and four random characters at the end.

Replace vowels with special symbols:

a → @

e → #

i → $

o → %

u → &

Case 2: Word length is less than 3 characters

Reverse the word.

Decoding Rules

For each word in the encoded message:

Case 1: Word length is 3 or more characters

Remove four characters from the start and four characters from the end.

Take the last three characters and move them to the beginning.

Replace special symbols back to vowels:

@ → a

→ e

$ → i

% → o

& → u

Case 2: Word length is less than 3 characters

Reverse the word.

How to Run

Ensure Python 3 is installed on your system.

Clone the repository:

git clone https://github.com/your-username/secret-code-language.git


Navigate to the project directory:

cd secret-code-language


Run the program:

python secret_code.py

Usage

After running the program, you will be prompted to choose an operation:

What you want to do 'ENCODE' OR 'DECODE' :


Enter the desired option and then provide the message when prompted.

Notes

Encoded output varies each time due to random character selection.

Decoding works correctly only for text encoded using this program.

All input text is converted to lowercase.

Technologies Used

Python 3

random module

Author

Yash Sharma
