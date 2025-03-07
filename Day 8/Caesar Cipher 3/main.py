from art import logo
import math
# TODO-1: Import and print the logo from art.py when the program starts.
# import "art.py"
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
import re
# regex=re.compile("/\[0-9]\s/g")
# regex = re.compile(r"[^\w\s]")

try:
    def caesar(original_text, shift_amount, encode_or_decode):
        flag=False
        should_continue=False
        output_text = ""
        while(should_continue!=True):
            for letter in original_text:
                if encode_or_decode == "decode":
                    shift_amount *= -1
                try:
                    shifted_position = alphabet.index(letter) + shift_amount
                    shifted_position %= len(alphabet)
                    output_text += alphabet[shifted_position]
                except ValueError as ve:
                    print("invalid value please enter a word without whitespace or symbol")
                    flag=True
                    break
            if(flag==False):    
                print(f"Here is the {encode_or_decode}d result: {output_text}")
            userinput = input("Yes if you want to continue No if you don't = \n").lower()
            if(userinput=="yes"):
                should_continue=False
            else:
                should_continue=True
                break
except ValueError as ve:
    print("invalid value")

# TODO-3: Can you figure out a way to restart the cipher program?


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
# if(len(re.findall("/\W/g",text))):
    # print("invalidcharacter value")
# print(re.findall("/\w/g",text))
# print("yes there is a number symbol character",regex.search(text))
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



