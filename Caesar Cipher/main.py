from alphabet import alphabet
to_continue = True

while to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26

    def caesar(text, shift, direction):
        encrypted_text = ""
        if direction == "decode":
                shift *= -1
        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift
                encrypted_text += alphabet[new_position] 
            else:
                encrypted_text += char         
        print(f"The {direction} text is {encrypted_text}")
        
    caesar(text, shift, direction)
    user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if user_input == "no":
        to_continue = False
        print("Goodbye")




    
    