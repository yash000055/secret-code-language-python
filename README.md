# Secret Code Language Translator using Python
A simple Python program that encodes and decodes English text into a secret code language using string manipulation and random characters.

## How It Works :

-When you run the program, it asks:
-ENCODE or DECODE

## Encoding Rules :

-If word length ≥ 3:
-Move first 3 letters to the end
-Add random characters at start & end
-Replace vowels:
a	e	i	o	u
@	#	$	%	&

-If word length < 3:
Reverse the word

## Decoding Rules :

-If word length ≥ 3:
-Remove random characters from start & end
-Move last 3 letters to the beginning
-Replace symbols back to vowels
-If word length < 3:
Reverse the word

## Run the Program :
-python secret_code.py

## Tech Used :
-Python 3
-random module
