PLACEHOLDER="[name]"
with open("./Input/Names/invited_names.txt")as names:
    name=names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    content=letter.read()
    for i in name:
        stripped_name=i.strip()
        new_content=content.replace(PLACEHOLDER,stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode='w') as output:
            output.write(new_content)



#TODO: Create a letter using starting_letter.txt 

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp