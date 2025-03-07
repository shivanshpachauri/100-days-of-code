alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# print(len(text))
# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text,shift_amount):
        ciphertext=""
        for i in original_text:
            position=alphabet.index(i)+shift_amount
            if(position>25):
                 position=position-26
            ciphertext+=alphabet[position]
        print(f" output for encrypted letter {ciphertext}")

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
def decrypt(original_text,shift_amount):
        ciphertext=""
        for i in original_text:
            position=alphabet.index(i)-shift_amount
            ciphertext+=alphabet[position]
        print(f" output for decrypted letter {ciphertext}")

if(direction=='encode'):
    encrypt(text,shift)
elif(direction=='decode'):
    decrypt(text,shift)

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

